import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QTextBrowser, QLineEdit, QMenu, QToolTip
from PyQt5.QtCore import Qt, QUrl, QPoint
from PyQt5.QtGui import QFont, QTextCursor, QClipboard
from PyQt5 import uic
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QDesktopServices
import sqlite3


class Memo(QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize sqlite
        self.conn = sqlite3.connect('memo.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT, hidden INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hidden_texts (id INTEGER PRIMARY KEY, note_id INTEGER, position INTEGER, text TEXT)''')
        self.conn.commit()

        self.textEdit = QTextBrowser(self)
        self.hidden_texts = {}
        
        self.textEdit.setStyleSheet("border: none;")

        # load ui file
        uic.loadUi('memo.ui', self)

        self.load_notes()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #button connect to func 
        self.closebutton.clicked.connect(self.close_application)#close 
        self.smallbutton.clicked.connect(self.minimize_application)#minimize

        self.boldbutton.clicked.connect(self.toggle_bold)  # bolder
        self.dialogsbutton.clicked.connect(self.toggle_task_checkbox)  # dialogs(buged)
        self.eyebutton.clicked.connect(self.toggle_hide_text)  # hiding text(buged:when open again lose message)
        self.linkbutton.clicked.connect(self.convert_to_link)  # link button

        #make the button can be clicked
        self.boldbutton.setCheckable(True)
        self.boldbutton.clicked.connect(self.toggle_bold)  
        self.textEdit.textChanged.connect(self.set_font_for_new_input)  
        self.dialogsbutton.setCheckable(True)  
        self.eyebutton.setCheckable(True)  
        self.linkbutton.setCheckable(True) 

        # can be drag (resizing hasn't be set)
        self.is_dragging = False
        self.is_resizing = False
        self.resize_margin = 10  

    def save_note_to_db(self):
        #save to db
        current_text = self.textEdit.toPlainText()
        print(f"Saving note to database: {current_text}")  # test message
        
        # Save note content
        self.cursor.execute("DELETE FROM notes WHERE id=1")  
        self.cursor.execute("INSERT INTO notes (id, text) VALUES (1, ?)", (current_text,))
        
        # Save hidden text information
        self.cursor.execute("DELETE FROM hidden_texts WHERE note_id=1")
        for pos, text in self.hidden_texts.items():
            self.cursor.execute("INSERT INTO hidden_texts (note_id, position, text) VALUES (1, ?, ?)", (pos, text))
        
        self.conn.commit()

    def load_notes(self):
        #load from db
        self.cursor.execute("SELECT * FROM notes WHERE id=1")
        result = self.cursor.fetchone()
        if result:
            print(f"Loaded note from database: {result[1]}")  # test message
            self.textEdit.setPlainText(result[1])  
            
            # Load hidden text information
            self.hidden_texts = {}
            self.cursor.execute("SELECT position, text FROM hidden_texts WHERE note_id=1")
            hidden_results = self.cursor.fetchall()
            for pos, text in hidden_results:
                self.hidden_texts[pos] = text
        else:
            print("No notes found in the database.")  

    def closeEvent(self, event):
        #saving when close
        self.save_note_to_db()
        event.accept()

    def close_application(self):
        self.close()  # close button

    def minimize_application(self):
        self.showMinimized()

    def toggle_bold(self):#bold
        cursor = self.textEdit.textCursor()

        if cursor.hasSelection():

            char_format = cursor.charFormat()
            current_font = char_format.font()

            if self.boldbutton.isChecked():
                current_font.setWeight(QFont.Bold) 
            else:
                current_font.setWeight(QFont.Normal)  

            char_format.setFont(current_font)
            cursor.mergeCharFormat(char_format) 
            self.textEdit.setTextCursor(cursor)

    def set_font_for_new_input(self):
        cursor = self.textEdit.textCursor()

        char_format = cursor.charFormat()
        current_font = char_format.font()

        if self.boldbutton.isChecked(): 
            current_font.setWeight(QFont.Bold) 
        else:
            current_font.setWeight(QFont.Normal)

        char_format.setFont(current_font)

        self.textEdit.blockSignals(True)  # stop textChanged 
        cursor.mergeCharFormat(char_format)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.blockSignals(False)  # recover textChanged 

    def toggle_task_checkbox(self):
        cursor = self.textEdit.textCursor()
        
        # Check if there is selected text
        if cursor.hasSelection():
            selected_text = cursor.selectedText()
            # If the selected text is a checkbox, toggle its state
            if selected_text in ["☐", "☑"]:
                if selected_text == "☐":
                    cursor.insertText("☑")
                else:
                    cursor.insertText("☐")
                return
        
        # If there is no selected text or the selected text is not a checkbox, insert a checkbox at the cursor position
        cursor.insertText("☐")
        
        # Update cursor position
        self.textEdit.setTextCursor(cursor)

    def toggle_hide_text(self):
        cursor = self.textEdit.textCursor()
        if cursor.hasSelection():
            selected_text = cursor.selectedText()
            start_pos = cursor.selectionStart()  # get position
            end_pos = cursor.selectionEnd()  

            # if not hide then hide
            if selected_text != "■" * len(selected_text):
                self.hidden_texts[start_pos] = selected_text  
                cursor.insertText('■' * len(selected_text)) 
            else:
                # recover
                if start_pos in self.hidden_texts:
                    original_text = self.hidden_texts[start_pos]  
                    cursor.insertText(original_text)  
                    del self.hidden_texts[start_pos]

    def convert_to_link(self):
        cursor = self.textEdit.textCursor()
        
        if cursor.hasSelection():
            selected_text = cursor.selectedText()
            
            # Check if it's a URL
            if selected_text.startswith(("http://", "https://", "www.")):
                # Save original URL
                if not hasattr(self, 'url_positions'):
                    self.url_positions = {}
                
                # Get insertion position
                pos = cursor.position()
                
                # Insert short link text
                cursor.insertText("🖇️ Link")
                
                # Save URL and position information
                self.url_positions[pos] = selected_text
                
                # Update cursor position
                self.textEdit.setTextCursor(cursor)
                
                # Add mouse hover event handler
                self.textEdit.mouseMoveEvent = self.custom_mouse_move_event
                
                # Add mouse click event handler
                self.textEdit.mousePressEvent = self.custom_mouse_press_event
                
                # Add right-click menu event handler
                self.textEdit.contextMenuEvent = self.custom_context_menu_event
    
    def custom_mouse_move_event(self, event):
        # Get text cursor at mouse position
        cursor = self.textEdit.cursorForPosition(event.pos())
        pos = cursor.position()
        
        # Check if there is a link
        if hasattr(self, 'url_positions'):
            for url_pos, url in self.url_positions.items():
                if url_pos <= pos <= url_pos + len("🖇️ Link"):
                    # Show tooltip
                    self.textEdit.setToolTip(url)
                    return
        
        # If not on a link, clear tooltip
        self.textEdit.setToolTip("")
    
    def custom_mouse_press_event(self, event):
        # Get text cursor at mouse position
        cursor = self.textEdit.cursorForPosition(event.pos())
        pos = cursor.position()
        
        # Check if there is a link
        if hasattr(self, 'url_positions'):
            for url_pos, url in self.url_positions.items():
                if url_pos <= pos <= url_pos + len("🖇️ Link"):
                    # Create a QLineEdit to display and select URL
                    url_display = QLineEdit(self)
                    url_display.setText(url)
                    url_display.setReadOnly(True)
                    url_display.setGeometry(event.pos().x(), event.pos().y() + 20, 300, 20)
                    url_display.show()
                    url_display.selectAll()
                    url_display.setFocus()
                    return
        
        # If not on a link, call original mousePressEvent
        QTextEdit.mousePressEvent(self.textEdit, event)
    
    def custom_context_menu_event(self, event):
        # Get text cursor at mouse position
        cursor = self.textEdit.cursorForPosition(event.pos())
        pos = cursor.position()
        
        # Check if there is a link
        if hasattr(self, 'url_positions'):
            for url_pos, url in self.url_positions.items():
                if url_pos <= pos <= url_pos + len("🖇️ Link"):
                    # Create right-click menu
                    menu = QMenu(self)
                    copy_action = menu.addAction("Copy Link")
                    open_action = menu.addAction("Open Link")
                    
                    # Show menu
                    action = menu.exec_(event.globalPos())
                    
                    if action == copy_action:
                        # Copy URL to clipboard
                        clipboard = QApplication.clipboard()
                        clipboard.setText(url)
                    elif action == open_action:
                        # Open URL
                        QDesktopServices.openUrl(QUrl(url))
                    
                    return
        
        # If not on a link, call original contextMenuEvent
        QTextEdit.contextMenuEvent(self.textEdit, event)

    def mousePressEvent(self, event):
        self.drag_position = event.globalPos()

        if event.x() >= self.width() - self.resize_margin and event.y() >= self.height() - self.resize_margin:
            self.is_resizing = True
            self.setCursor(Qt.SizeFDiagCursor) 
        else:
            self.is_dragging = True
            self.setCursor(Qt.ArrowCursor)  

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            delta = event.globalPos() - self.drag_position
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.drag_position = event.globalPos()
        else:
            # Get text cursor at mouse position
            cursor = self.textEdit.cursorForPosition(event.pos())
            pos = cursor.position()
            
            # Check if there is a link
            if hasattr(self, 'url_positions'):
                for url_pos, url in self.url_positions.items():
                    if url_pos <= pos <= url_pos + len("🖇️ Link"):
                        self.textEdit.setToolTip(url)
                        return
            
            # If not on a link, clear tooltip
            self.textEdit.setToolTip("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Memo()
    window.show()
    sys.exit(app.exec_())
