# Sounds of Space: MRO CRISM Sonification Project
Python script that sonifies satellite hyperspectral images of Mars.

This project was developed during the NASA SpaceApps 2023 Challenge for the track "Immersed in the Sounds of Space" The challenge took place on 7-8 October 2023.

For more details about the challenge, visit [SpaceApps Challenge](https://www.spaceappschallenge.org/2023/challenges/immersed-in-the-sounds-of-space/?tab=details).

## Demo
https://github.com/andrii0yerko/Sounds-of-Space/assets/46103860/8cb052bc-5715-4f3a-8c69-8f65fd767f0b


## Project Description

This Python-based software project aims to sonify data from the MRO CRISM (Compact Reconnaissance Imaging Spectrometer for Mars) [MULTISPECTRAL REDUCED DATA RECORD V1.0](https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-5-RDR-MULTISPECTRAL-V1.0) dataset, and potentially any other [MRO CRISM records](https://arcnav.psi.edu/urn:nasa:pds:context:instrument:crism.mro). Sonification, in this context, involves converting hyperspectral images into piano music. This software offers a unique auditory approach to the scientific analysis of CRISM data.

## Solution Algorithm

- The software sonifies CRISM data by transforming it into a musical composition.
- It reduces the size of the 3D data, ensuring that the resulting soundtrack is manageable in terms of duration, using averaging by sliding windows.
- The software assigns musical attributes to the data: the x-coordinate becomes the timing of musical notes, the mean of the channels corresponds to pitch (higher values result in higher-pitched notes), and duration is inversely related to the mean (higher values result in shorter notes).
- The standard deviation of the channels influences the volume or intensity of the notes.
- The sonified data is exported to MIDI format that can be rendered using a piano or any other instrument.
