# 5. Write a class that keeps track of the number of instances created.
class InstanceCounter:
    """
    A class that keeps track of the number of instances created.
    """
    # Class variable to store the count of instances
    _instance_count = 0

    def __init__(self, name=""):
        """
        Constructor for InstanceCounter.
        Increments the instance count each time a new object is created.
        """
        self.name = name  # Optional attribute for instance identification
        InstanceCounter._instance_count += 1
        print(f"Instance '{self.name}' created. Total instances: {InstanceCounter._instance_count}")

    @classmethod
    def get_instance_count(cls):
        """
        Class method to get the total number of instances created.
        """
        return cls._instance_count

# --- Demonstration ---

# Create instances of the class
print("Creating instances:")
instance1 = InstanceCounter("First")
instance2 = InstanceCounter("Second")
instance3 = InstanceCounter("Third")

# Get the total count using the class method
current_count = InstanceCounter.get_instance_count()
print(f"\nTotal instances created so far: {current_count}")

# Create more instances
instance4 = InstanceCounter("Fourth")
instance5 = InstanceCounter("Fifth")

# Get the updated count
updated_count = InstanceCounter.get_instance_count()
print(f"\nTotal instances created after more additions: {updated_count}")

# You can also access the class variable directly, though a method is often preferred for encapsulation
print(f"Directly accessing class variable: {InstanceCounter._instance_count}")









