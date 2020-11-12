# Application Programming Interfaces

![fatdog](assets/fatdog.jpg)

## Interfacing with Applications through Programming

API stands for Application Programming Interface, which is a sort of almost meaninglessly broad set of words. The important part is "interface": APIs are a broad set of concepts that involve defining the boundaries between things.

In a programing sense, an interface for describes what something should do while an implementation describes how that something will do it. This should be familiar already, since it's been a common theme in CodeLab: we can think of a function call as the basic components of an interface and, so long as we know what arguments to pass it, we don't have to know how to actually do it. We'll talk a little more about this in a moment. Often, the documentation for, say, a software library is referred to interchangably with "API" since the interface is most of what users of a library care about.

So, APIs is a pretty big tent of different ideas. They are used for such different things as:
Programming languages (Oracle v. Google)
Libraries
Databases
Hardware and hardware-adjacent things
File systems
Operating systems
Web APIs

As we can see from this list, APIs are often defined in common ways so as to function as formal or de facto standards. But they don't have to be - they can be totally customized to unique purposes.

Abstraction and Modularity
Class examples

Web APIs
Originally: the internet was intended to be a collection of static documents with unique addresses: URL = uniform resource locator.
Fairly quickly, people started to create dynamic content.
Early years were a bit of a wild west and we can still see evidence of this on older sites: CGI, mod-php
Web services
REST - "Representational state transfer" method, not standard
    stateless
    return to the basic representation of the original Internet: resources addressible by identifiers, but with resources that aren't necessarily statically generated or unchanging
    well-formed response

API key, secret, token
API version numbers
API Limits
