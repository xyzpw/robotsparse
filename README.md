# robotsparse
A python package that enhances speed and simplicity of parsing robots files.

## Usage
Basic usage, such as getting robots contents:
```python
import robotsparse

#NOTE: The `find_url` parameter will redirect the url to the default robots location.
robots = robotsparse.urlRobots("https://github.com/", find_url=True)
print(list(robots)) # output: ['user-agents']
```
The `user-agents` key will contain each user-agent found in the robots file contents along with information associated with them.<br>

Alternatively, we can assign the robots contents as an object, which allows faster accessability:
```python
import robotsparse

# This function returns a class.
robots = robotsparse.getRobots("https://duckduckgo.com/", find_url=True)
assert isinstance(robots, object)
print(robots.allow) # Prints allowed locations
print(robots.disallow) # Prints disallowed locations
print(robots.crawl_delay) # Prints found crawl-delays
print(robots.robots) # This output is equivalent to the above example
```

