import win32com.client
import time

def main():
    """
    This script disables a specific CAN message from a specific node in Vector Canoe.
    """
    try:
        # Connect to the Canoe application
        canoe_app = win32com.client.Dispatch("CANoe.Application")

        # Check if a measurement is running
        if not canoe_app.Measurement.Running:
            print("Measurement is not running. Please start a measurement in Canoe first.")
            return

        print("Successfully connected to Canoe.")

        # --- Configuration ---
        # Replace with your actual node and message names
        node_name = "YourNodeName"  # e.g., "Gateway"
        message_name = "YourMessageName" # e.g., "EngineStatus"
        # ---------------------

        # Access the simulation setup
        simulation = canoe_app.Configuration.SimulationSetup

        # Find the specified node in the simulation setup
        node = None
        for n in simulation.Nodes:
            if n.Name == node_name:
                node = n
                break
        
        if node is None:
            print(f"Error: Node '{node_name}' not found in the simulation setup.")
            print("Available nodes are:")
            for n in simulation.Nodes:
                print(f"- {n.Name}")
            return

        # Find the specified message in the node's transmit messages
        message = None
        for msg in node.TxMessages:
            if msg.Name == message_name:
                message = msg
                break

        if message is None:
            print(f"Error: Transmit message '{message_name}' not found for node '{node_name}'.")
            print("Available transmit messages for this node are:")
            for msg in node.TxMessages:
                print(f"- {msg.Name}")
            return

        # Disable the message by setting its 'Enabled' property to False
        if message.Enabled:
            message.Enabled = False
            print(f"Successfully disabled message '{message_name}' from node '{node_name}'.")
        else:
            print(f"Message '{message_name}' from node '{node_name}' was already disabled.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nPlease ensure that:")
        print("1. Vector Canoe is installed and a configuration is loaded.")
        print("2. A measurement is currently running in Canoe.")
        print("3. The 'pywin32' library is installed (`pip install pywin32`).")
        print("4. The script is run with the correct permissions to access COM objects.")
        print("5. The node and message names in the script match your Canoe configuration exactly.")

if __name__ == "__main__":
    main()
