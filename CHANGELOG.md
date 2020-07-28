# Version 0.4.1 (2020-07-28)

## New features
 * None

## Enhancements
 * None

## Bug Fixes
* Fix issue #13 where upload to pypi on release was failing due to 
  long description change. 

## Doc Changes
* Updated the CHANGELOG.md to correct the new feature entry to point 
  to the correct github issue.

## Test/CI Enhancements
* None


# Version 0.4.0 (2020-07-28)

## New features
 * Added support for running openstack commands on a remote host
   using a context manager. Addresses issue #6 

## Enhancements
None

## Bug Fixes
* None

## Doc Changes
* Updated README to show the examples of using the `remote_shell` context
  manager

## Test/CI Enhancements
* Added some test coverage for the new context manager logic


# Version 0.3.0 (2020-07-16)

## New features
None

## Enhancements
None

## Bug Fixes
* Fix issue #7 where we could not delete multiple resources of the same type
  and did not have a specific key to specify in the dictionary of options
  for a target resource when doing add/remove commands.

## Doc Changes
* Updated README to have better examples of building the dictionary of command
  options

## Test/CI Enhancements
* None


# Version 0.2.0 (2020-07-06)

## New features
None

## Enhancements
* Changed decorator logging to only happen in debug
* Removed the proxy initiation loggin from the shell 

## Bug Fixes
* None

## Doc Changes
* Updated README to be clearer and fix grammar typos

## Test/CI Enhancements
* None


# Version 0.1.0 (2020-07-01)

## New features
* First initial release of the ospclientsdk
* Supports all openstack client commands

## Enhancements
* None

## Bug Fixes
* None

## Doc Changes
* None

## Test/CI Enhancements
* None