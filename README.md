# Empty/Dummy service for Home Assistant
Empty/Dummy service for Home Assistant. Useful in case of complex automations when in specific case within automation service template no actual service to be trigered.


## Integration installation
In `/config` folder create `custom_components` folder and load source files folder `none` in it. In 'configuration.yaml' include:
```
none:
```

## Services
### Service: archive.file
`none.none` is a dummy service that does nothing and can accept any number of attributes without any errors.

#### Example 1
```
service: none.none
data:
  file: '/config/image_snapshot/photo.png'
```

#### Example 2
```
service: none.none
data:
```
