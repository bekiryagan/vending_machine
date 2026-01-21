# =============================================================================
# Object-Oriented Programming in Python - Drink Management System
# =============================================================================
# Author: OOP Exam Project
# Description: A comprehensive demonstration of OOP concepts including
#              inheritance, encapsulation, polymorphism, and composition.
# =============================================================================


class Drink:
    """
    Base class for all beverages.
    
    This class serves as the foundation for all drink types in the system.
    It encapsulates the common properties and behaviors that all drinks share.
    
    Attributes:
        volume (int): The volume of the drink in milliliters.
        expiration (int): The number of days until the drink expires.
    
    Methods:
        next_day(): Simulates the passage of one day, reducing expiration.
        is_expired(): Checks if the drink has expired.
    """
    
    def __init__(self, volume: int, expiration: int):
        """
        Initialize a new Drink object.
        
        Args:
            volume (int): Volume in milliliters.
            expiration (int): Days until expiration.
        """
        self.volume = volume
        self.expiration = expiration
    
    def next_day(self):
        """
        Simulate the passage of one day.
        Reduces the expiration counter by 1 if the drink hasn't expired yet.
        """
        if self.expiration > 0:
            self.expiration -= 1
        else:
            print(f"Warning: {self.__class__.__name__} has already expired!")
    
    def is_expired(self) -> bool:
        """
        Check if the drink has expired.
        
        Returns:
            bool: True if expired, False otherwise.
        """
        return self.expiration <= 0
    
    def __str__(self) -> str:
        """Return a string representation of the drink."""
        return f"{self.__class__.__name__}: {self.volume}mL, expires in {self.expiration} days"
    
    def __repr__(self) -> str:
        """Return a detailed representation for debugging."""
        return f"{self.__class__.__name__}(volume={self.volume}, expiration={self.expiration})"


class Juice(Drink):
    """
    Subclass of Drink representing fruit juices.
    
    Fruit juices have a fixed expiration period of 7 days (one week),
    regardless of other factors. This demonstrates inheritance with
    modified default behavior.
    
    Attributes:
        volume (int): The volume of the juice in milliliters.
        expiration (int): Always set to 7 days.
        fruit_type (str): Optional fruit type for the juice.
    """
    
    DEFAULT_EXPIRATION = 7  # Class constant for juice expiration
    
    def __init__(self, volume: int, fruit_type: str = "Mixed"):
        """
        Initialize a new Juice object.
        
        Args:
            volume (int): Volume in milliliters.
            fruit_type (str): Type of fruit (default: "Mixed").
        """
        super().__init__(volume, self.DEFAULT_EXPIRATION)
        self.fruit_type = fruit_type
    
    def __str__(self) -> str:
        """Return a string representation of the juice."""
        return f"Juice ({self.fruit_type}): {self.volume}mL, expires in {self.expiration} days"


class DataCola(Drink):
    """
    Subclass of Drink representing DataCola beverages.
    
    DataCola drinks come in two container types, each with predefined
    volume and expiration values. This demonstrates inheritance with
    conditional initialization based on parameters.
    
    Container Types:
        - 'can': 330mL, 60 days expiration
        - 'bottle': 500mL, 30 days expiration
    
    Attributes:
        volume (int): Determined by container type.
        expiration (int): Determined by container type.
        container (str): The container type ('can' or 'bottle').
    """
    
    # Class constants for container specifications
    CONTAINER_SPECS = {
        'can': {'volume': 330, 'expiration': 60},
        'bottle': {'volume': 500, 'expiration': 30}
    }
    
    def __init__(self, container: str):
        """
        Initialize a new DataCola object.
        
        Args:
            container (str): Container type ('can' or 'bottle').
        
        Raises:
            ValueError: If container type is not 'can' or 'bottle'.
        """
        if container not in self.CONTAINER_SPECS:
            raise ValueError(f"Invalid container type: {container}. Use 'can' or 'bottle'.")
        
        specs = self.CONTAINER_SPECS[container]
        super().__init__(specs['volume'], specs['expiration'])
        self.container = container
    
    def __str__(self) -> str:
        """Return a string representation of the DataCola."""
        return f"DataCola: {self.volume}mL, expires in {self.expiration} days, in a {self.container}"


class EnergyDrink(Drink):
    """
    Subclass of Drink representing energy drinks.
    
    Energy drinks have caffeine content and come in different sizes.
    This class demonstrates additional attributes beyond the base class.
    
    Attributes:
        volume (int): Volume in milliliters.
        expiration (int): Days until expiration.
        caffeine_mg (int): Caffeine content in milligrams.
        sugar_free (bool): Whether the drink is sugar-free.
    """
    
    def __init__(self, volume: int, expiration: int, caffeine_mg: int = 80, sugar_free: bool = False):
        """
        Initialize a new EnergyDrink object.
        
        Args:
            volume (int): Volume in milliliters.
            expiration (int): Days until expiration.
            caffeine_mg (int): Caffeine content in mg (default: 80).
            sugar_free (bool): Sugar-free variant (default: False).
        """
        super().__init__(volume, expiration)
        self.caffeine_mg = caffeine_mg
        self.sugar_free = sugar_free
    
    def __str__(self) -> str:
        """Return a string representation of the energy drink."""
        sugar_status = "Sugar-Free" if self.sugar_free else "Regular"
        return f"EnergyDrink ({sugar_status}): {self.volume}mL, {self.caffeine_mg}mg caffeine, expires in {self.expiration} days"


class Water(Drink):
    """
    Subclass of Drink representing bottled water.
    
    Water has a very long shelf life and can be sparkling or still.
    This demonstrates inheritance with simplified attributes.
    
    Attributes:
        volume (int): Volume in milliliters.
        expiration (int): Days until expiration (default: 365 days).
        sparkling (bool): Whether the water is sparkling.
    """
    
    DEFAULT_EXPIRATION = 365  # Water lasts a long time
    
    def __init__(self, volume: int, sparkling: bool = False):
        """
        Initialize a new Water object.
        
        Args:
            volume (int): Volume in milliliters.
            sparkling (bool): Sparkling water (default: False).
        """
        super().__init__(volume, self.DEFAULT_EXPIRATION)
        self.sparkling = sparkling
    
    def __str__(self) -> str:
        """Return a string representation of the water."""
        water_type = "Sparkling" if self.sparkling else "Still"
        return f"Water ({water_type}): {self.volume}mL, expires in {self.expiration} days"


class VendingMachine:
    """
    A class representing a vending machine that manages drinks.
    
    This class demonstrates composition - it contains and manages
    multiple Drink objects. It provides methods to add, remove,
    and maintain the drinks inventory.
    
    Attributes:
        content (list): List of Drink objects in the machine.
        size (int): Maximum capacity of the machine.
        name (str): Name/location identifier for the machine.
    
    Methods:
        add(drink): Add a drink to the machine.
        remove(i): Remove drink at index i.
        verify(): Remove all expired drinks.
        next_day(): Age all drinks by one day.
        get_inventory(): Get a summary of current inventory.
        find_by_type(drink_type): Find drinks by their type.
    """
    
    def __init__(self, size: int, name: str = "Vending Machine"):
        """
        Initialize a new VendingMachine.
        
        Args:
            size (int): Maximum number of drinks the machine can hold.
            name (str): Name/location identifier (default: "Vending Machine").
        """
        self.content = []
        self.size = size
        self.name = name
    
    def add(self, drink: Drink) -> bool:
        """
        Add a drink to the vending machine.
        
        Args:
            drink (Drink): The drink to add.
        
        Returns:
            bool: True if added successfully, False if machine is full.
        """
        if len(self.content) < self.size:
            self.content.append(drink)
            print(f"Added {drink} to {self.name}.")
            return True
        else:
            print(f"Cannot add {drink}. {self.name} is full!")
            return False
    
    def remove(self, i: int) -> Drink:
        """
        Remove a drink from the vending machine by index.
        
        Args:
            i (int): Index of the drink to remove.
        
        Returns:
            Drink: The removed drink, or None if index is invalid.
        """
        if 0 <= i < len(self.content):
            removed_drink = self.content.pop(i)
            print(f"Removed {removed_drink} from {self.name}.")
            return removed_drink
        else:
            print(f"Invalid index: {i}. No drink removed.")
            return None
    
    def verify(self) -> list:
        """
        Check for and remove all expired drinks.
        
        Returns:
            list: List of removed expired drinks.
        """
        expired_drinks = []
        # Iterate backwards to safely remove items
        for i in range(len(self.content) - 1, -1, -1):
            if self.content[i].is_expired():
                expired_drinks.append(self.content.pop(i))
        
        if expired_drinks:
            print(f"Removed {len(expired_drinks)} expired drink(s) from {self.name}.")
        else:
            print(f"No expired drinks found in {self.name}.")
        
        return expired_drinks
    
    def next_day(self):
        """
        Simulate the passage of one day for all drinks.
        Ages all drinks and then verifies for expired items.
        """
        for drink in self.content:
            drink.next_day()
        print(f"All drinks in {self.name} have aged by one day.")
    
    def get_inventory(self) -> dict:
        """
        Get a summary of the current inventory by drink type.
        
        Returns:
            dict: Dictionary with drink types as keys and counts as values.
        """
        inventory = {}
        for drink in self.content:
            drink_type = drink.__class__.__name__
            inventory[drink_type] = inventory.get(drink_type, 0) + 1
        return inventory
    
    def find_by_type(self, drink_type: type) -> list:
        """
        Find all drinks of a specific type.
        
        Args:
            drink_type (type): The class type to search for.
        
        Returns:
            list: List of drinks matching the type.
        """
        return [drink for drink in self.content if isinstance(drink, drink_type)]
    
    def total_volume(self) -> int:
        """
        Calculate the total volume of all drinks.
        
        Returns:
            int: Total volume in milliliters.
        """
        return sum(drink.volume for drink in self.content)
    
    def __str__(self) -> str:
        """Return a string representation of the vending machine."""
        output = [f"\n{self.name} (capacity: {self.size}, current: {len(self.content)})"]
        output.append("=" * 50)
        for i, drink in enumerate(self.content):
            output.append(f"  [{i}] {drink}")
        if not self.content:
            output.append("  [Empty]")
        output.append("=" * 50)
        return "\n".join(output)
    
    def __len__(self) -> int:
        """Return the number of drinks in the machine."""
        return len(self.content)


# =============================================================================
# EXAMPLE 1: Basic Usage - Creating and Managing Drinks
# =============================================================================

def example_1_basic_usage():
    """
    Demonstrates basic creation and manipulation of drink objects.
    Shows inheritance, method calls, and basic OOP concepts.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Usage - Creating and Managing Drinks")
    print("=" * 70)
    
    # Create different types of drinks
    print("\n--- Creating Drinks ---")
    basic_drink = Drink(500, 10)
    orange_juice = Juice(1000, "Orange")
    apple_juice = Juice(750, "Apple")
    cola_can = DataCola('can')
    cola_bottle = DataCola('bottle')
    
    # Display all drinks
    drinks = [basic_drink, orange_juice, apple_juice, cola_can, cola_bottle]
    for drink in drinks:
        print(f"  {drink}")
    
    # Demonstrate next_day method
    print("\n--- Simulating 3 Days Passing ---")
    for day in range(1, 4):
        print(f"\nDay {day}:")
        for drink in drinks:
            drink.next_day()
            print(f"  {drink}")
    
    # Check expiration status
    print("\n--- Expiration Status ---")
    for drink in drinks:
        status = "EXPIRED" if drink.is_expired() else "Fresh"
        print(f"  {drink.__class__.__name__}: {status}")


# =============================================================================
# EXAMPLE 2: Vending Machine Operations
# =============================================================================

def example_2_vending_machine():
    """
    Demonstrates the VendingMachine class with full CRUD operations.
    Shows composition, inventory management, and expiration handling.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Vending Machine Operations")
    print("=" * 70)
    
    # Create a vending machine
    vm = VendingMachine(6, "Campus Vending Machine")
    
    # Add various drinks
    print("\n--- Stocking the Vending Machine ---")
    vm.add(Drink(350, 5))
    vm.add(Juice(500, "Grape"))
    vm.add(DataCola('can'))
    vm.add(DataCola('bottle'))
    vm.add(EnergyDrink(250, 30, 150, True))
    vm.add(Water(500, True))
    
    # Display initial state
    print(vm)
    
    # Show inventory summary
    print("\n--- Inventory Summary ---")
    inventory = vm.get_inventory()
    for drink_type, count in inventory.items():
        print(f"  {drink_type}: {count}")
    print(f"  Total Volume: {vm.total_volume()}mL")
    
    # Simulate time passing until a drink expires
    print("\n--- Simulating 5 Days ---")
    for day in range(5):
        vm.next_day()
    
    print(vm)
    
    # Verify and remove expired drinks
    print("\n--- Checking for Expired Drinks ---")
    expired = vm.verify()
    
    print(vm)
    
    # Find specific drink types
    print("\n--- Finding DataCola Products ---")
    colas = vm.find_by_type(DataCola)
    for cola in colas:
        print(f"  Found: {cola}")


# =============================================================================
# EXAMPLE 3: Multiple Vending Machines Network
# =============================================================================

def example_3_vending_network():
    """
    Demonstrates managing multiple vending machines as a network.
    Shows advanced OOP concepts like object collections and aggregation.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Vending Machine Network Management")
    print("=" * 70)
    
    # Create a network of vending machines
    machines = [
        VendingMachine(5, "Library Machine"),
        VendingMachine(8, "Cafeteria Machine"),
        VendingMachine(4, "Gym Machine")
    ]
    
    # Stock each machine differently
    print("\n--- Stocking Machines ---")
    
    # Library: Quiet drinks (water, juice)
    machines[0].add(Water(500))
    machines[0].add(Water(500, True))
    machines[0].add(Juice(330, "Apple"))
    machines[0].add(Juice(330, "Orange"))
    
    # Cafeteria: Variety
    machines[1].add(DataCola('can'))
    machines[1].add(DataCola('bottle'))
    machines[1].add(Juice(500, "Tropical"))
    machines[1].add(EnergyDrink(500, 45, 160))
    machines[1].add(Water(1000))
    machines[1].add(Drink(350, 2))  # Short expiration for demo
    
    # Gym: Energy and water
    machines[2].add(EnergyDrink(250, 60, 200, True))
    machines[2].add(EnergyDrink(500, 60, 300))
    machines[2].add(Water(750))
    machines[2].add(Water(750, True))
    
    # Display all machines
    for machine in machines:
        print(machine)
    
    # Network statistics
    print("\n--- Network Statistics ---")
    total_drinks = sum(len(m) for m in machines)
    total_volume = sum(m.total_volume() for m in machines)
    total_capacity = sum(m.size for m in machines)
    
    print(f"  Total Machines: {len(machines)}")
    print(f"  Total Drinks: {total_drinks}")
    print(f"  Total Capacity: {total_capacity}")
    print(f"  Utilization: {total_drinks/total_capacity*100:.1f}%")
    print(f"  Total Volume: {total_volume}mL ({total_volume/1000:.1f}L)")
    
    # Simulate a week
    print("\n--- Simulating One Week ---")
    for day in range(7):
        for machine in machines:
            machine.next_day()
    print("One week has passed...")
    
    # Check all machines for expired drinks
    print("\n--- Weekly Maintenance Check ---")
    total_expired = 0
    for machine in machines:
        expired = machine.verify()
        total_expired += len(expired)
    print(f"\nTotal expired drinks removed: {total_expired}")
    
    # Final state
    print("\n--- Final Network State ---")
    for machine in machines:
        print(f"  {machine.name}: {len(machine)}/{machine.size} drinks")


# =============================================================================
# EXAMPLE 4: Advanced Features - Polymorphism Demo
# =============================================================================

def example_4_polymorphism():
    """
    Demonstrates polymorphism - treating different objects uniformly.
    Shows how different drink types respond to the same method calls.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Polymorphism Demonstration")
    print("=" * 70)
    
    # Create a mixed collection of drinks
    drinks = [
        Drink(500, 3),
        Juice(750, "Mango"),
        DataCola('can'),
        EnergyDrink(250, 5, 120, True),
        Water(1000, False)
    ]
    
    print("\n--- Polymorphic Behavior ---")
    print("All drinks respond to the same methods differently:\n")
    
    # Same method call, different behavior (polymorphism)
    for drink in drinks:
        print(f"  Type: {drink.__class__.__name__:15} | {drink}")
    
    print("\n--- Using isinstance() for Type Checking ---")
    for drink in drinks:
        if isinstance(drink, DataCola):
            print(f"  {drink.__class__.__name__}: Container = {drink.container}")
        elif isinstance(drink, Juice):
            print(f"  {drink.__class__.__name__}: Fruit = {drink.fruit_type}")
        elif isinstance(drink, EnergyDrink):
            print(f"  {drink.__class__.__name__}: Caffeine = {drink.caffeine_mg}mg")
        elif isinstance(drink, Water):
            print(f"  {drink.__class__.__name__}: Sparkling = {drink.sparkling}")
        else:
            print(f"  {drink.__class__.__name__}: Basic drink")
    
    print("\n--- Inheritance Chain ---")
    for drink in drinks:
        print(f"  {drink.__class__.__name__} inherits from: {drink.__class__.__bases__[0].__name__}")


# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("#" + " " * 68 + "#")
    print("#" + "  OBJECT-ORIENTED PROGRAMMING - DRINK MANAGEMENT SYSTEM  ".center(68) + "#")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    
    # Run all examples
    example_1_basic_usage()
    example_2_vending_machine()
    example_3_vending_network()
    example_4_polymorphism()
    
    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("=" * 70)
