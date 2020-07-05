SERVICE_NONE = "none"
DOMAIN = "none"

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    
    def handle_empty(call):
        """Handle the service call."""
        return True

    hass.services.register(DOMAIN, SERVICE_NONE, handle_empty)
    # Return boolean to indicate that initialization was successfully.
    return True