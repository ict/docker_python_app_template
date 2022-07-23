# Python App Docker Template

This is a simple template for a dockerized python app. It takes care of

- Defining a set of options with default values
- Overriding options based on environment values and startup parameters (via `argparse`)
- Setting up basic logging and outputting some startup info so you know what is going on