from text_editor import TextEditor
from history import History

editor = TextEditor()
history = History()

editor.write("Привіт")
history.backup(editor.save())

editor.write(", світ!")
history.backup(editor.save())

editor.write(" Це тест.")
print("Поточний текст:", editor.get_text())

editor.restore(history.undo())
print("Після одного:", editor.get_text())

editor.restore(history.undo())
print("Після другого:", editor.get_text())
