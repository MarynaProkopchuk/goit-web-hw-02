from abc import ABC, abstractmethod
from bot_classes import BotCommands, AddressBook,Record

class Bot(ABC):
    @abstractmethod
    def return_all_users(self, book):
        pass
    @abstractmethod
    def return_help(self):
        pass

class SimpleBot(Bot):
    def return_all_users(self, book = AddressBook()):
        return "\n".join([str(record) for record in book.data.values()])

    def return_help(self):
        return "\n".join(BotCommands.commands_list)

class TableBot(Bot):
    def return_all_users(self, book = AddressBook()):
        contacts_list=""
        for number, contact in enumerate(("\n".join([str(record) for record in book.data.values()])).split("\n"),1):
            contacts_list += f"|{number:^5} |" + f"{contact:<60}|" + "\n"
        return contacts_list
    
    def return_help(self):
        all_commands=""
        for number, command in enumerate(BotCommands.commands_list, 1):
            all_commands += f"|{number:^5} |" + f"{command:<60}|" + "\n"
        return all_commands

bot = TableBot()