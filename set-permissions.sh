#!/bin/bash
# This script sets the correct permissions for the media and static directories.
# It is intended to be run on the host machine, not inside the container.

# The user that runs the application in the container.
# See Dockerfile.
APP_USER=wagtail

# The directories that need to be writable by the application.
# See docker-compose.yml.
MEDIA_DIR=./media
STATIC_DIR=./static

# Create the directories if they don't exist.
mkdir -p $MEDIA_DIR
mkdir -p $STATIC_DIR

# Set the ownership of the directories to the user that runs the application.
# This is necessary so the application can write to these directories.
chown -R $APP_USER:$APP_USER $MEDIA_DIR
chown -R $APP_USER:$APP_USER $STATIC_DIR

# Set the permissions of the directories.
# The owner should have read, write, and execute permissions.
# The group and others should have read and execute permissions.
chmod -R 755 $MEDIA_DIR
chmod -R 755 $STATIC_DIR
