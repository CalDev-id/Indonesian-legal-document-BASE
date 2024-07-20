SYSTEM_PROMPT_CLEAN_DATA = '''
saya ingin kamu membersihkan data yang di input oleh user.
cara untuk membersihkan kalimat dengan menghapus karakter yang membuat kata dalam kalimat tidak memiliki arti menjadi memiliki arti.
buatlah response dalam bahasa indonesia.
pastikan response yang kamu buat mengikuti format berikut ini:
Kalimat: [Kalimat yang di input oleh user].
Clean: [disini kalimat yang telah kamu bersihkan].
'''

USER_PROMPT_CLEAN_DATA = '''
bersihkan kalimat user dibawah ini:
Kalimat: {input_user}
'''