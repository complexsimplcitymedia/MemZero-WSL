#!/usr/bin/env python3
"""
Command-line interface for the LEGO Fortress Builder

This CLI allows users to build and manage LEGO-style block fortresses
for the MemZero-WSL system.
"""

import sys
from block import Block, MemoryBlock, ProcessorBlock, StorageBlock
from fortress import Fortress


def create_demo_fortress():
    """
    Create a demonstration fortress with stacked blocks.
    
    Returns:
        Fortress: A pre-built fortress for demonstration
    """
    fortress = Fortress("AI-Blocking Fortress")
    
    # Create foundation blocks with varying protection levels
    memory_block_1 = MemoryBlock(size=100, protection_level=5)
    memory_block_2 = MemoryBlock(size=150, protection_level=7)
    processor_block = ProcessorBlock(size=80, protection_level=6)
    
    # Add foundation blocks
    fortress.add_foundation_block(memory_block_1)
    fortress.add_foundation_block(memory_block_2)
    fortress.add_foundation_block(processor_block)
    
    # Stack additional blocks on top
    storage_block_1 = StorageBlock(size=120, protection_level=8)
    fortress.stack_on_block(0, storage_block_1)
    
    memory_block_3 = MemoryBlock(size=90, protection_level=9)
    fortress.stack_on_block(0, memory_block_3)
    
    processor_block_2 = ProcessorBlock(size=60, protection_level=10)
    fortress.stack_on_block(1, processor_block_2)
    
    storage_block_2 = StorageBlock(size=200, protection_level=7)
    fortress.stack_on_block(2, storage_block_2)
    
    return fortress


def interactive_mode():
    """Run the fortress builder in interactive mode."""
    print("=== LEGO Fortress Builder ===")
    print("Build your modular fortress with stackable blocks!\n")
    
    fortress_name = input("Enter fortress name (or press Enter for 'My Fortress'): ").strip()
    if not fortress_name:
        fortress_name = "My Fortress"
    
    fortress = Fortress(fortress_name)
    
    print(f"\nBuilding '{fortress_name}'...\n")
    
    while True:
        print("\nOptions:")
        print("1. Add a foundation block")
        print("2. Stack a block on existing foundation")
        print("3. Display fortress structure")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            add_foundation_block_interactive(fortress)
        elif choice == "2":
            stack_block_interactive(fortress)
        elif choice == "3":
            print("\n" + str(fortress))
        elif choice == "4":
            print("\nFinal fortress structure:")
            print(str(fortress))
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def add_foundation_block_interactive(fortress):
    """Interactive helper to add a foundation block."""
    print("\nBlock types:")
    print("1. Memory Block")
    print("2. Processor Block")
    print("3. Storage Block")
    
    block_type = input("Select block type (1-3): ").strip()
    
    try:
        size = int(input("Enter block size: "))
        protection = int(input("Enter protection level (0-10): "))
        
        if block_type == "1":
            block = MemoryBlock(size, protection)
        elif block_type == "2":
            block = ProcessorBlock(size, protection)
        elif block_type == "3":
            block = StorageBlock(size, protection)
        else:
            print("Invalid block type!")
            return
        
        fortress.add_foundation_block(block)
        print(f"\n✓ Added {block}")
    except ValueError:
        print("Invalid input! Please enter numbers for size and protection level.")


def stack_block_interactive(fortress):
    """Interactive helper to stack a block on existing foundation."""
    if not fortress.foundation_blocks:
        print("\nNo foundation blocks yet! Add a foundation block first.")
        return
    
    print("\nAvailable foundations:")
    for i, block in enumerate(fortress.foundation_blocks):
        print(f"{i+1}. {block}")
    
    try:
        foundation_index = int(input("\nSelect foundation number to stack on: ")) - 1
        
        if foundation_index < 0 or foundation_index >= len(fortress.foundation_blocks):
            print("Invalid foundation number!")
            return
        
        print("\nBlock types:")
        print("1. Memory Block")
        print("2. Processor Block")
        print("3. Storage Block")
        
        block_type = input("Select block type (1-3): ").strip()
        size = int(input("Enter block size: "))
        protection = int(input("Enter protection level (0-10): "))
        
        if block_type == "1":
            block = MemoryBlock(size, protection)
        elif block_type == "2":
            block = ProcessorBlock(size, protection)
        elif block_type == "3":
            block = StorageBlock(size, protection)
        else:
            print("Invalid block type!")
            return
        
        fortress.stack_on_block(foundation_index, block)
        print(f"\n✓ Stacked {block}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except IndexError as e:
        print(f"Error: {e}")


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        # Demo mode: create and display a pre-built fortress
        print("Creating demonstration fortress...\n")
        fortress = create_demo_fortress()
        print(fortress)
        print("\nThis fortress blocks out AI with maximum protection level:", 
              fortress.get_max_protection_level())
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
