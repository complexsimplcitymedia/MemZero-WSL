#!/usr/bin/env python3
"""
Tests for the LEGO Fortress system
"""

from block import Block, MemoryBlock, ProcessorBlock, StorageBlock
from fortress import Fortress


def test_block_creation():
    """Test basic block creation."""
    print("Testing block creation...")
    
    block = Block("test", 100, 5)
    assert block.block_type == "test"
    assert block.size == 100
    assert block.protection_level == 5
    assert len(block.blocks_above) == 0
    
    memory_block = MemoryBlock(200, 7)
    assert memory_block.block_type == "memory"
    assert memory_block.size == 200
    
    print("✓ Block creation tests passed")


def test_block_stacking():
    """Test stacking blocks."""
    print("Testing block stacking...")
    
    base = Block("base", 100, 5)
    top = Block("top", 50, 3)
    
    assert base.stack(top)
    assert len(base.blocks_above) == 1
    assert base.get_total_height() == 2
    
    # Stack another block
    top2 = Block("top2", 30, 2)
    base.stack(top2)
    assert base.get_total_height() == 3
    
    print("✓ Block stacking tests passed")


def test_block_total_size():
    """Test total size calculation."""
    print("Testing total size calculation...")
    
    base = Block("base", 100, 5)
    top = Block("top", 50, 3)
    top2 = Block("top2", 30, 2)
    
    base.stack(top)
    top.stack(top2)
    
    assert base.get_total_size() == 180  # 100 + 50 + 30
    
    print("✓ Total size tests passed")


def test_fortress_creation():
    """Test fortress creation and management."""
    print("Testing fortress creation...")
    
    fortress = Fortress("Test Fortress")
    assert fortress.name == "Test Fortress"
    assert len(fortress.foundation_blocks) == 0
    assert fortress.total_blocks == 0
    
    print("✓ Fortress creation tests passed")


def test_fortress_foundation():
    """Test adding foundation blocks to fortress."""
    print("Testing fortress foundations...")
    
    fortress = Fortress("Test Fortress")
    
    block1 = MemoryBlock(100, 5)
    block2 = ProcessorBlock(150, 7)
    
    assert fortress.add_foundation_block(block1)
    assert fortress.add_foundation_block(block2)
    assert len(fortress.foundation_blocks) == 2
    assert fortress.total_blocks == 2
    
    print("✓ Fortress foundation tests passed")


def test_fortress_stacking():
    """Test stacking blocks in fortress."""
    print("Testing fortress stacking...")
    
    fortress = Fortress("Test Fortress")
    
    base = MemoryBlock(100, 5)
    fortress.add_foundation_block(base)
    
    top = StorageBlock(50, 3)
    fortress.stack_on_block(0, top)
    
    assert fortress.total_blocks == 2
    assert len(base.blocks_above) == 1
    
    print("✓ Fortress stacking tests passed")


def test_fortress_metrics():
    """Test fortress metrics calculations."""
    print("Testing fortress metrics...")
    
    fortress = Fortress("Test Fortress")
    
    block1 = MemoryBlock(100, 5)
    block2 = ProcessorBlock(150, 7)
    block3 = StorageBlock(200, 10)
    
    fortress.add_foundation_block(block1)
    fortress.add_foundation_block(block2)
    fortress.stack_on_block(0, block3)
    
    assert fortress.get_total_size() == 450  # 100 + 150 + 200
    assert fortress.get_max_protection_level() == 10
    assert fortress.total_blocks == 3
    
    print("✓ Fortress metrics tests passed")


def test_complex_fortress():
    """Test a complex fortress structure."""
    print("Testing complex fortress...")
    
    fortress = Fortress("Complex Fortress")
    
    # Create multiple foundations
    mem1 = MemoryBlock(100, 5)
    mem2 = MemoryBlock(150, 7)
    proc1 = ProcessorBlock(80, 6)
    
    fortress.add_foundation_block(mem1)
    fortress.add_foundation_block(mem2)
    fortress.add_foundation_block(proc1)
    
    # Stack multiple levels
    storage1 = StorageBlock(120, 8)
    fortress.stack_on_block(0, storage1)
    
    mem3 = MemoryBlock(90, 9)
    fortress.stack_on_block(0, mem3)
    
    proc2 = ProcessorBlock(60, 10)
    fortress.stack_on_block(1, proc2)
    
    # Verify structure
    assert fortress.total_blocks == 6
    assert fortress.get_max_protection_level() == 10
    assert fortress.get_total_size() == 100 + 150 + 80 + 120 + 90 + 60
    
    print("✓ Complex fortress tests passed")


def run_all_tests():
    """Run all tests."""
    print("=" * 50)
    print("Running LEGO Fortress System Tests")
    print("=" * 50)
    print()
    
    test_block_creation()
    test_block_stacking()
    test_block_total_size()
    test_fortress_creation()
    test_fortress_foundation()
    test_fortress_stacking()
    test_fortress_metrics()
    test_complex_fortress()
    
    print()
    print("=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
