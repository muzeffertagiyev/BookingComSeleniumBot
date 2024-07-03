import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests


email_api_endpoint = 'https://api.npoint.io/700baf4dcaef21388e91'

response = requests.get(email_api_endpoint)
email_data = response.json()

sender_email = email_data['sender_email']['email']
sender_password = email_data['sender_email']['password']


class EmailSend:

    def __init__(self,collection,to_email):
        self.collection = collection
        self.html_content = self.generate_html_content(self.collection)
        self.to_email = to_email

    def generate_html_content(self,collection):
        html_output = '''
            <html>
            <head>
                <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th, td {
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                    tr:nth-child(even) {
                        background-color: #f9f9f9;
                    }
                    programmer {
                        color:green;
                        bold:700;
                    }
                </style>
            </head>
            <body>
                <h2>Hello , Please find below information about hotels as per your request city</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Hotel Name</th>
                            <th>Price</th>
                            <th>Score</th>
                            <th>Link</th>
                        </tr>
                    </thead>
                    <tbody>
            '''

        for hotel in collection:
            hotel_html = f"""
            <tr>
                <td>{hotel['name']}</td>
                <td>{hotel['price']}</td>
                <td>{hotel['score']}</td>
                <td><a href="{hotel['link']}">View Hotel Result</a></td>
            </tr>
            """
            html_output += hotel_html

        html_output += '''
                </tbody>
            </table>

            <h3>Have a nice staying. </h3>
            <h3>Information has been sent by Selenium bot which has been created by <span class='programmer'>
            <a href='https://www.linkedin.com/in/muzaffar-taghiyev/'>Muzaffar Taghiyev</a>
            </span> </h3>
        </body>
        </html>
        '''
        return html_output


    def send_email(self,subject):
        
        with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
            
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)

            message = MIMEMultipart("alternative")
            message['From'] = sender_email
            message['To'] = self.to_email
            message['Subject'] = subject

            # Add HTML content to the message
            html_part = MIMEText(self.html_content, "html")
            message.attach(html_part)
            
            connection.sendmail(from_addr=sender_email, to_addrs=self.to_email, msg=message.as_string())


