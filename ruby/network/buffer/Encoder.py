from ruby.network.buffer.BufferArray import BufferArray


class Encoder:

    @staticmethod
    def encoder(message):
        if type(message) is str:
            return message.encode()
        else:
            output = message
            buffer_array = output.bufferArray
            packet = BufferArray()
            for token in output.output:
                packet.writeByte(token)
            packet.writeBytes(buffer_array.toByteArray())

            length = len(packet) + len(output.output)
            p2 = BufferArray()
            if 0xFF >= length:
                p2.writeByte(1)
                p2.writeByte(length)
            elif 0xFFFF >= length:
                p2.writeByte(2)
                p2.writeShort(length)
            else:
                p2.writeByte(3)
                p2.writeByte(length >> 16)
                p2.writeByte(length >> 8)
                p2.writeByte(length >> 0)
            p2.writeBytes(packet.toByteArray())
            return p2.toByteArray()