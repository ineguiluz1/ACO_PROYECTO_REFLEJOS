class MicroProtocols:
    @staticmethod
    def encode_command(command, params=None):
        if params:
            return f"{command}:{','.join(map(str, params))}\n"
        return f"{command}\n"

    @staticmethod
    def decode_command(command):
        return command.split(':')
