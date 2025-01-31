import numpy as np
import numpy.ma as ma
import xml.etree.ElementTree as ET


def read_xml(file):
    """
    Converts trajectory datasets from XML files to numpy arrays formatted
    for diffpy
    """

    tree = ET.parse(file)
    root = tree.getroot()

    # Get the number of frames
    frames = 0
    particles = 0
    for child in root:
        nspots = int(child.attrib['nSpots'])
        if nspots > frames:
            frames = nspots
        particles += 1
    #print(frames)
    #print(particles)

    # Create numpy arrays
    xs = np.ones((frames, particles))*np.nan
    ys = np.ones((frames, particles))*np.nan

    # Read in data
    part = 0
    for child in root:
        frame = 0
        for particle in child:
            #print(particle.tag, particle.attrib)
            xs[frame, part] = float(particle.attrib['x'])
            ys[frame, part] = float(particle.attrib['y'])
            frame += 1
        part += 1

    return xs, ys
