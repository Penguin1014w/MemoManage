import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QTextBrowser
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QTextCursor
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
        self.cursor.execute("DELETE FROM notes WHERE id=1")  
        self.cursor.execute("INSERT INTO notes (id, text) VALUES (1, ?)", (current_text,))
        self.conn.commit()

    def load_notes(self):
        #load from db
        self.cursor.execute("SELECT * FROM notes WHERE id=1")
        result = self.cursor.fetchone()
        if result:
            print(f"Loaded note from database: {result[1]}")  # test message
            self.textEdit.setPlainText(result[1])  
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




    def toggle_task_checkbox(self):#(bug!!)
        cursor = self.textEdit.textCursor()
    
        # check the position of cursor
        cursor.select(QTextCursor.WordUnderCursor) 
    
        selected_text = cursor.selectedText()
    
        if selected_text == "☑":

            cursor.insertText("☐")  
        else:

            cursor.insertText("☑")  
        self.textEdit.setTextCursor(cursor)


    def toggle_hide_text(self):
        cursor = self.textEdit.textCursor()
        if cursor.hasSelection():
            selected_text = cursor.selectedText()
            start_pos = cursor.selectionStart()  # get postion
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

    def convert_to_link(self): #not finish
        pass
            # cursor = self.textEdit.textCursor()

            # if cursor.hasSelection():
            #     selected_text = cursor.selectedText()

            #     if selected_text.startswith("http"): 
            #        
            #         cursor.insertHtml(f'<a href="{selected_text}" title="{selected_text}">🖇️ Link</a>')


    

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
            




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Memo()
    window.show()
    sys.exit(app.exec_())
