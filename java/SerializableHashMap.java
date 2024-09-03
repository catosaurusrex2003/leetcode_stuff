import java.nio.ByteBuffer;
import java.util.Arrays;

public class SerializableHashMap {
    private byte[] byteArray;
    private int pageSize;
    private int numPages;

    // Initialize the hash map
    public void init(int pageSize, int numPages) {
        this.pageSize = pageSize;
        this.numPages = numPages;
        this.byteArray = new byte[pageSize * numPages + 18]; // 18 bytes for the header
        System.arraycopy(intToBytes(pageSize), 0, byteArray, 0, 4);
        System.arraycopy(intToBytes(numPages), 0, byteArray, 4, 4);
    }

    // GET command
    public int get(int key) {
        if (key == 1 || key == 0) {
            int flagIndex = (key == 1) ? 8 : 13;
            if (byteArray[flagIndex] == 1) {
                int valueIndex = (key == 1) ? 9 : 14;
                return bytesToInt(Arrays.copyOfRange(byteArray, valueIndex, valueIndex + 4));
            } else {
                return 0;
            }
        } else {
            int pageIndex = key % numPages;
            int pageStart = 18 + pageIndex * pageSize;
            for (int i = 0; i < pageSize; i += 8) {
                int storedKey = bytesToInt(Arrays.copyOfRange(byteArray, pageStart + i, pageStart + i + 4));
                if (storedKey == key) {
                    return bytesToInt(Arrays.copyOfRange(byteArray, pageStart + i + 4, pageStart + i + 8));
                } else if (storedKey == 0) {
                    return 0;
                }
            }
        }
        return 0;
    }

    // PUT command
    public void put(int key, int value) {
        if (key == 1 || key == 0) {
            int flagIndex = (key == 1) ? 8 : 13;
            int valueIndex = (key == 1) ? 9 : 14;
            byteArray[flagIndex] = 1;
            System.arraycopy(intToBytes(value), 0, byteArray, valueIndex, 4);
        } else {
            int pageIndex = key % numPages;
            int pageStart = 18 + pageIndex * pageSize;
            for (int i = 0; i < pageSize; i += 8) {
                int storedKey = bytesToInt(Arrays.copyOfRange(byteArray, pageStart + i, pageStart + i + 4));
                if (storedKey == key) {
                    System.arraycopy(intToBytes(value), 0, byteArray, pageStart + i + 4, 4);
                    return;
                } else if (storedKey == 0 || storedKey == 1) {
                    System.arraycopy(intToBytes(key), 0, byteArray, pageStart + i, 4);
                    System.arraycopy(intToBytes(value), 0, byteArray, pageStart + i + 4, 4);
                    return;
                }
            }
            throw new RuntimeException("No space left in the page to insert the key");
        }
    }

    // DELETE command
    public void delete(int key) {
        if (key == 1 || key == 0) {
            int flagIndex = (key == 1) ? 8 : 13;
            int valueIndex = (key == 1) ? 9 : 14;
            byteArray[flagIndex] = 0;
            Arrays.fill(byteArray, valueIndex, valueIndex + 4, (byte) 0);
        } else {
            int pageIndex = key % numPages;
            int pageStart = 18 + pageIndex * pageSize;
            for (int i = 0; i < pageSize; i += 8) {
                int storedKey = bytesToInt(Arrays.copyOfRange(byteArray, pageStart + i, pageStart + i + 4));
                if (storedKey == key) {
                    System.arraycopy(intToBytes(1), 0, byteArray, pageStart + i, 4); // Set key to 1 (indicating
                                                                                     // deleted)
                    System.arraycopy(intToBytes(0), 0, byteArray, pageStart + i + 4, 4);
                    return;
                }
            }
        }
    }

    // DUMP command
    public void dump() {
        StringBuilder sb = new StringBuilder();

        // Header bytes (Page size, Number of pages, Special key flags, and values)
        sb.append(toHex(byteArray[0], byteArray[1], byteArray[2], byteArray[3])).append(" ");
        sb.append(toHex(byteArray[4], byteArray[5], byteArray[6], byteArray[7])).append(" ");
        sb.append(toHex(byteArray[8])).append(" ");
        sb.append(toHex(byteArray[9], byteArray[10], byteArray[11], byteArray[12])).append(" ");
        sb.append(toHex(byteArray[13])).append(" ");
        sb.append(toHex(byteArray[14], byteArray[15], byteArray[16], byteArray[17])).append(" ");

        // Pages content
        int pageStart = 18;
        for (int page = 0; page < numPages; page++) {
            sb.append(" [");
            for (int offset = 0; offset < pageSize; offset += 8) {
                int key = ByteBuffer.wrap(byteArray, pageStart + offset, 4).getInt();
                int value = ByteBuffer.wrap(byteArray, pageStart + offset + 4, 4).getInt();
                if (key == 1) {
                    sb.append("ffffffff:00000000");
                } else {
                    sb.append(String.format("%08x", key)).append(":").append(String.format("%08x", value));
                }
                if (offset + 8 < pageSize)
                    sb.append(",");
            }
            sb.append(",]");
            pageStart += pageSize;
        }

        System.out.println(sb.toString().trim());
    }

    private String toHex(byte... bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            hexString.append(String.format("%02x", b));
        }
        return hexString.toString();
    }

    // Utility method: Convert int to bytes (Big Endian)
    private byte[] intToBytes(int value) {
        return new byte[] {
                (byte) (value >> 24),
                (byte) (value >> 16),
                (byte) (value >> 8),
                (byte) value
        };
    }

    // Utility method: Convert bytes to int (Big Endian)
    private int bytesToInt(byte[] bytes) {
        return ((bytes[0] & 0xFF) << 24) |
                ((bytes[1] & 0xFF) << 16) |
                ((bytes[2] & 0xFF) << 8) |
                (bytes[3] & 0xFF);
    }

    // Main method to test the implementation
    public static void main(String[] args) {
        SerializableHashMap hashMap = new SerializableHashMap();
        hashMap.init(16, 4);
        hashMap.put(12, 255);
        // hashMap.delete(12);
        hashMap.dump();
        System.out.println(hashMap.get(12));
    }
}