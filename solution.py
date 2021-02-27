from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   # Fill in start
   #smtpServer = ("127.0.0.1", 1025)
   smtpServer = ("smtp.nyu.edu", 25)
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect(smtpServer)
   # Fill in end

   #recv = clientSocket.recv(1024).decode()
   #print(recv)
   #if recv[:3] != '220':
   #    print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
   #    print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   emailFromCommand = 'MAIL FROM:<cem10000@nyu.edu>\r\n'
   clientSocket.send(emailFromCommand.encode())
   recv2 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
   #    print('250 reply not received from server.')
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   emailToCommand = 'RCPT TO:<cem10000@nyu.edu>\r\n'
   clientSocket.send(emailToCommand.encode())
   recv3 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
   #    print('250 reply not received from server.')
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   emailDataCommand = 'DATA\r\n'
   clientSocket.send(emailDataCommand.encode())
   recv4 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
   #    print('emailDataCommand: 250 reply not received from server.')
   # Fill in end

   # Send message data.
   # Fill in start
   emailMessageDataCommand = msg
   clientSocket.send(emailMessageDataCommand.encode())
   #recv1 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
   #    print('emailMessageDataCommand: 250 reply not received from server.')
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   emailMessageDataEndCommand = endmsg
   clientSocket.send(emailMessageDataEndCommand.encode())
   #recv1 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
   #    print('emailMessageDataEndCommand: 250 reply not received from server.')
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   emailQuitCommand = 'QUIT\r\n'
   clientSocket.send(emailQuitCommand.encode())
   recv5 = clientSocket.recv(1024).decode()
   print(recv1)
   #if recv1[:3] != '250':
   #    print('250 reply not received from server.')
   clientSocket.close()
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')