# This is a Client for our Tic-Tac-Toe game. It will communicate over TCP or UDP (user choice) with the server.
import socket
import threading
import uuid
import sys          # Use sys.argv to get command line arguments
import atexit       # For sending the server a "quit" message when the client is closed


# Define constants
LOGGING = 1 # 0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file
TCP_PORT = 3116
UDP_PORT = 31161

CONNECTION_TYPE = {
	"TCP": "TCP",
	"UDP": "UDP"
}

class Client:
	def __init__(self, connection_type, hostname=None, logging=LOGGING):
		self.id = uuid.uuid4().hex
		self.running = False
		self.version = 0     # Should be 1 or 2
		self.protocol = None
		self.game_code = None
		self.game_id = None
		self.connection_type = None
		self.logging = logging
		if not hostname:
			self.hostname = socket.gethostname()
		else:
			self.hostname = hostname

		self.socket = None

		# Sockets and threading
		self.receive_thread = None
		self.send_thread = None
		self.receive_socket = None
		self.send_socket = None
		self.udp_socket = None

		self.udp_receive_socket = None
		self.udp_send_socket = None

		self.tcp_receive_socket = None
		self.tcp_send_socket = None

		self._connect(connection_type)

		self._handle_keyboard_input()

	def _connect(self, connection_type):
		# Check if the client requests to use TCP or UDP.
		if connection_type == CONNECTION_TYPE['TCP']:
			# Create the two sockets: one for receiving and one for sending
			self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			# Connect the sockets to the server
			self.receive_socket.connect((self.hostname, TCP_PORT))
			self.send_socket.connect((self.hostname, TCP_PORT))

		else:
			self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			# Connect the sockets to the server
			self.receive_socket.connect((self.hostname, UDP_PORT))
			self.send_socket.connect((self.hostname, UDP_PORT))

		# Create the threads for receiving and sending data
		self.receive_thread = threading.Thread(target=self._receive_data, args=(connection_type,))
		self.send_thread = threading.Thread(target=self._send_data, args=(connection_type,))

	def _receive_data(self, connection_type):
		# This is a socket handler that will run in a separate thread to handle incoming data from the server.
		# Depending on the connection type, it will handle the data differently.
		if connection_type == CONNECTION_TYPE['TCP']:
			while True:
				data = self.receive_socket.recv(1024)
				if self.logging == 1:
					sys.stdout.write('Receiving TCP Message: ')
				sys.stdout.write(str(data.decode()))
				# print(data.decode())
		else:
			# This is a UDP connection
			while True:
				data = self.receive_socket.recvfrom(1024)
				if self.logging == 1:
					sys.stdout.write('Receiving UDP Message: ')
				sys.stdout.write(str(data.decode()))
				# print(data.decode())

	def _send_data(self, connection_type):
		# This is a socket handler that we will set up to send data to the server.
		# Depending on the connection type, it will handle the data differently.
		if connection_type == CONNECTION_TYPE['TCP']:
			while True:
				data = input('Enter a message: ')
				print('Sending TCP Message: ' + data)
				self.send_socket.sendall(data.encode())
		else:
			# This is a UDP connection
			while True:
				data = input('Enter a message: ')
				print('Sending UDP Message: ' + data)
				self.send_socket.sendto(data.encode(), (self.hostname, UDP_PORT))

	def _handle_keyboard_input(self):
		"""
		This is a while loop that will run in a separate thread to handle keyboard input from the user during the course of the game.
		Potential commands are:
		"quit" - Quit the game
		"restart" - Restart the game
		:return:
		:rtype:
		"""
		while self.running:
			# Get keyboard input from the user
			user_input = input("\nEnter a command: ")

			# Parse the command
			command = user_input.split(" ")[0]

			print("\nYou entered: " + command)

			command = command.upper()

			# Handle the command
			if command == "BORD":
				pass
			elif command == "CREA":
				pass
			elif command == "GAMS":
				pass
			elif command == "GDBY":
				pass
			elif command == "HELO":
				pass
			elif command == "JOIN":
				pass
			elif command == "JOND":
				pass
			elif command == "LIST":
				pass
			elif command == "MOVE":
				pass
			elif command == "QUIT":
				# Send message to the server
				pass
			elif command == "SESS":
				pass
			elif command == "TERM":
				pass
			elif command == "YRMV":
				pass
			elif command == "TEST":
				print("TEST")
			else:
				print("Invalid command.")

	def _restart_game(self):
		pass