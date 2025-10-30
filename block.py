"""
LEGO-style Block System for MemZero-WSL

This module provides a modular, stackable block architecture for building
memory management components in a composable way.
"""


class Block:
    """
    Base class representing a modular block in the system.
    
    Blocks can be stacked together to create more complex structures (fortresses).
    Each block has a type, size, and optional protection level.
    """
    
    def __init__(self, block_type, size, protection_level=0):
        """
        Initialize a new block.
        
        Args:
            block_type (str): The type of block (e.g., 'memory', 'processor', 'storage')
            size (int): The size of the block in arbitrary units
            protection_level (int): Security/protection level (0-10)
        """
        self.block_type = block_type
        self.size = size
        self.protection_level = protection_level
        self.blocks_above = []
    
    def stack(self, other_block):
        """
        Stack another block on top of this one.
        
        Args:
            other_block (Block): The block to stack on top
            
        Returns:
            bool: True if stacking was successful
        """
        if not isinstance(other_block, Block):
            raise TypeError("Can only stack Block instances")
        
        self.blocks_above.append(other_block)
        return True
    
    def get_total_height(self):
        """
        Calculate the total height of this block and all blocks stacked above it.
        
        Returns:
            int: Total number of blocks in the stack
        """
        height = 1
        for block in self.blocks_above:
            height += block.get_total_height()
        return height
    
    def get_total_size(self):
        """
        Calculate the total size of this block and all blocks stacked above it.
        
        Returns:
            int: Total size of all blocks in the stack
        """
        total = self.size
        for block in self.blocks_above:
            total += block.get_total_size()
        return total
    
    def __repr__(self):
        return f"Block(type={self.block_type}, size={self.size}, protection={self.protection_level})"
    
    def __str__(self):
        stack_info = f" with {len(self.blocks_above)} blocks above" if self.blocks_above else ""
        return f"{self.block_type.capitalize()} Block (size: {self.size}, protection: {self.protection_level}){stack_info}"


class MemoryBlock(Block):
    """A specialized block for memory management."""
    
    def __init__(self, size, protection_level=0):
        super().__init__('memory', size, protection_level)


class ProcessorBlock(Block):
    """A specialized block for processor/computation tasks."""
    
    def __init__(self, size, protection_level=0):
        super().__init__('processor', size, protection_level)


class StorageBlock(Block):
    """A specialized block for storage management."""
    
    def __init__(self, size, protection_level=0):
        super().__init__('storage', size, protection_level)
