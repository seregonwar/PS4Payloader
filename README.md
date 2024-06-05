# Hen Installation Payload Sender

This Python script serves as a payload sender to install the Hen modification by sending a bin file over the local network to your console. Please note that the functionality of this program is not guaranteed at the moment, as it is still in the testing phase. However, you can test it using the Test Receiver, a client designed to intercept the packet within your local network.

## How to Use

1. **Test Receiver Setup**: First, set up the Test Receiver by following these steps:
    - Ensure you have the Test Receiver client installed.
    - Enter `127.0.0.1` as the sending IP address during the test setup. This IP is reserved for your PC and serves as the entry point.

2. **Run the Payload Sender**: Execute the payload sender script, providing the necessary parameters such as the bin file to be sent.

3. **Test with Test Receiver**: With the Test Receiver set up and the payload sender running, initiate the test. The bin file will be sent over the local network to the Test Receiver, which will intercept the packet.

4. **Verify**: Check the Test Receiver for the received payload. It should be saved with the name `payload.bin` in the same directory where the Test Receiver client is located.

## Important Note

- This program is currently in the testing phase, and its functionality may be limited or unstable.
- The bin file will not be executed on your PC during testing. Instead, it will be received and saved by the Test Receiver for verification purposes.

Please exercise caution when using this program, and feel free to provide feedback or report any issues encountered during testing. Your input will be valuable in further refining and improving the functionality of this payload sender.
