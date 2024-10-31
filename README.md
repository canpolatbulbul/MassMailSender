## How to use
This python script is useful for mass emailing a list of company emails for internship requests.

simply replace 
- `gmail_user` with your email 
- `gmail_password` with your app pasword
- edit the `subject` and `body` of email
- give CV's pdf name to `encode_cv(`"pdf_name_here"`)`

give a `contacts.txt` file with format:
```
email;name
email2;name2
```
and run the script with:

`python sendMail.py`

> [!IMPORTANT]
> Make sure  `contacts.txt` and  your CV pdf is in same folder as the script
