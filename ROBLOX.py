mail = imaplib.IMAP4_SSL(url, port=993) #default
mail.login(email,password)
mail.list()
mail.select("inbox")
typ, msgnums = mail.search(None, 'SUBJECT', '"Roblox Accounts Reminder"')