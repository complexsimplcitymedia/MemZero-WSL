"""
Fortress - A container for stacked LEGO-style blocks

This module provides the Fortress class which manages collections of
stacked blocks for the MemZero-WSL system.
"""

from block import Block


class Fortress:
    """
    A fortress is a collection of stacked blocks that provides
    protection and organization for memory management components.
    """
    
    def __init__(self, name):
        """
        Initialize a new fortress.
        
        Args:
            name (str): The name of this fortress
        """
        self.name = name
        self.foundation_blocks = []
        self.total_blocks = 0
    
    def add_foundation_block(self, block):
        """
        Add a foundation block to the fortress.
        
        Args:
            block (Block): The block to add as a foundation
            
        Returns:
            bool: True if the block was added successfully
        """
        if not isinstance(block, Block):
            raise TypeError("Can only add Block instances to fortress")
        
        self.foundation_blocks.append(block)
        self._update_total_blocks()
        return True
    
    def stack_on_block(self, foundation_index, new_block):
        """
        Stack a new block on top of an existing foundation block.
        
        Args:
            foundation_index (int): Index of the foundation block to stack on
            new_block (Block): The block to stack on top
            
        Returns:
            bool: True if stacking was successful
        """
        if foundation_index >= len(self.foundation_blocks):
            raise IndexError(f"Foundation block index {foundation_index} out of range")
        
        self.foundation_blocks[foundation_index].stack(new_block)
        self._update_total_blocks()
        return True
    
    def _update_total_blocks(self):
        """Update the total block count."""
        self.total_blocks = sum(block.get_total_height() for block in self.foundation_blocks)
    
    def get_total_size(self):
        """
        Get the total size of all blocks in the fortress.
        
        Returns:
            int: Total size of all blocks
        """
        return sum(block.get_total_size() for block in self.foundation_blocks)
    
    def get_max_protection_level(self):
        """
        Get the maximum protection level among all blocks.
        
        Returns:
            int: Maximum protection level
        """
        if not self.foundation_blocks:
            return 0
        
        max_protection = 0
        
        def check_protection(block):
            nonlocal max_protection
            max_protection = max(max_protection, block.protection_level)
            for b in block.blocks_above:
                check_protection(b)
        
        for block in self.foundation_blocks:
            check_protection(block)
        
        return max_protection
    
    def display_structure(self):
        """
        Display the fortress structure in a readable format.
        
        Returns:
            str: String representation of the fortress structure
        """
        lines = [f"=== {self.name} ==="]
        lines.append(f"Total blocks: {self.total_blocks}")
        lines.append(f"Total size: {self.get_total_size()}")
        lines.append(f"Max protection: {self.get_max_protection_level()}")
        lines.append("\nStructure:")
        
        for i, foundation in enumerate(self.foundation_blocks):
            lines.append(f"\nFoundation {i+1}:")
            lines.extend(self._display_block(foundation, indent=1))
        
        return "\n".join(lines)
    
    def _display_block(self, block, indent=0):
        """Helper method to recursively display block structure."""
        prefix = "  " * indent
        lines = [f"{prefix}└─ {block}"]
        
        for b in block.blocks_above:
            lines.extend(self._display_block(b, indent + 1))
        
        return lines
    
    def __repr__(self):
        return f"Fortress(name={self.name}, blocks={self.total_blocks}, foundations={len(self.foundation_blocks)})"
    
    def __str__(self):
        return self.display_structure()
