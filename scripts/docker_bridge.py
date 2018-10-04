"""
bridge to docker
"""

import logging
import docker

def container_ps():
    return docker.from_env().containers.list()

def container_create(name, data):
    """
    create container
    """
    logging.info('create ' + data['image'])

    if 'command' not in data:
        data['command'] = None
    if 'environment' not in data:
        data['environment'] = None
    if 'labels' not in data:
        data['labels'] = None
    if 'links' not in data:
        data['links'] = None
    if 'desktop' not in data:
        data['desktop'] = None

    return docker.from_env().containers.create(
        data['image'],
        command=data['command'],
        hostname=name,
        detach=True,
        user='user',
        environment=data['environment'],
        labels=data['labels'],
        links=data['links'],
        volumes_from=['desktop'])

def container_restart(name):
    """
    create container
    """
    logging.info('restart ' + name)
    return docker.from_env().containers.get(name).restart()

def image_get(name):
    """
    image get
    """

    return docker.from_env().images.get(name)


