const zlib = require('zlib');

// Base64 gzip/zlib compressed strings
const base64Strings = [
    "eJzzyc9Lyc8DAAgpAms=",
    "eJxzSi3KycwDAAfXAl0=",
    "eJzzSy1XiMwvygYADKUC8A=="
];

// Function to decode + decompress
function decodeAndDecompress(b64) {
    const compressedBuffer = Buffer.from(b64, 'base64');
    try {
        // Use zlib.inflateSync (works with zlib/deflate format)
        const result = zlib.inflateSync(compressedBuffer);
        return result.toString('utf-8');
    } catch (err) {
        return "Error decompressing: " + err.message;
    }
}

// Decode each Base64 string
base64Strings.forEach((b64, i) => {
    const city = decodeAndDecompress(b64);
    console.log(`String ${i + 1}: ${city}`);
});
