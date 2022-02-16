2022 Ideas Page
###############


:date: 2022-02-16
:modified: 2010-10-04 18:40
:tags: tardis, gsoc, ideas
:category: ideas page
:slug: tardis-gsoc-ideas
:authors: TARDIS-SN
:summary: Ideas Page

***************************
TARDIS GSoC 2022 Ideas Page
***************************

**Astronomy and Astrophysics Background:**

.. image:: {filename}images/480px-SN1994D.jpg
  :width: 400
  :alt: Alternative text

A `supernova <https://en.wikipedia.org/wiki/Supernova>`_ (here we show SN1994D in the Galaxy NGC4526 - image source: wikipedia) marks the brilliant death throes of
a star, during which it outshines its entire galaxy. It not only marks death, though: supernova ejecta change the
evolution of the universe and enable the formation of planets and life as we know it. From the iron in your blood to
the silicon in your laptop, supernovae return heavy elements assembled from the primordial hydrogen and helium left
after the big bang.

There are still many mysteries surrounding supernovae (e.g. their precise origins, inner workings, …). One way to study
these objects in more detail is to split the light coming from these objects into its components (like using a prism)
and analyzing the resulting data (which is called a spectrum). Here, we show spectra (black lines) of a number of
different supernova types (image courtesy Daniel Kasen and LBL). Different chemical elements present in the supernova
leave their mark on the spectra by imprinting characteristic features, so-called atomic lines (regions highlighted in
colour). Thus, studying and interpreting such spectra allows us to identify what supernovae are made of.

.. image:: {filename}images/sn_types.jpg
  :width: 800
  :alt: Alternative text

With sophisticated computer simulations astronomers try to reproduce the observed spectra to draw conclusion about the
properties of the supernova ejecta and ultimately the explosion mechanism and progenitor stars. TARDIS is such a
numerical code. It calculates theoretical spectra based on a number of input parameters, such as the supernova
brightness and the abundances of the different chemical elements present in the ejecta (e.g. Oxygen, Silicon, Iron,
etc.). The main idea for this procedure is that by finding a close match between theoretical and observed spectra we
identify the parameters that actually describe the supernovae.

******************
The TARDIS Project
******************

As mentioned in the background information above, TARDIS is a scientific tool (more specifically a Monte Carlo
radiative transfer code) whose primary goal is the calculation of theoretical spectra for supernovae. Below, you find
the typical result of a TARDIS calculation. It shows the calculated synthetic spectra for a simple supernova model.
This particular setup (tardis_example) is officially provided by the TARDIS collaboration on the
`documentation <https://tardis-sn.github.io/tardis/quickstart/quickstart.html>`_\.

.. image:: {filename}images/tardis_example.png
  :width: 800
  :alt: Alternative text

*******************************
List of GSoC 2022 Project Ideas
*******************************

In the TARDIS collaboration we first establish a detailed plan on implementing new features before starting the actual
work. This is an important step that ensures that the entire TARDIS collaboration is informed about the development
efforts and that the team members can help shape the ideas during the discussion phase. We call these documents TEP -
TARDIS Enhancement Proposals. We already have a great list of ideas at https://github.com/tardis-sn/tep that we need
help with. Some of these we have specially selected for GSoC 2022 and are listed with specific “warm-up” tasks below.
But feel free to propose your own TEP and make a PR on that.

If you use one of our TEPs, you can definitely add more detail to the implementation, but what we really want to see is
a detailed timeline with milestones that shows us that you have thought about how to implement the feature in three
months. For any questions about the projects, please ask on `Gitter <https://gitter.im/tardis-sn/gsoc>`_\.

Putting in a Pull Request with the First objective is essential for each proposal to allow to see how you work.

------------

**TARDIS Setups Framework**

**Difficulty:** Easy

**Astronomy Knowledge Needed:** None

**Mentors:** Ezequiel Passaro, Andrew Fullard

**Programming Skills Required** Python, GitHub Actions

**GSoC Application Tag:** setups

**Description:** Astrophysicists use TARDIS to create theoretical models of supernovae. One important aspect of these
models is the simulated spectrum. The features in the spectrum depend on details of the user's model, but also on the
atomic data and the physics implemented in TARDIS. However, since TARDIS is an actively developed code, this means that
new versions of the code may change the outputted simulated spectra from old projects. This project will focus on
developing an automated pipeline for running old models from scientific papers with new versions of the TARDIS code in
order to check that scientific inferences are still valid.


**Your first objective if you choose to accept the mission:** Download a model setup from the tardis-sn/tardis_setups
repository and run the simulation.  Plot the simulated spectrum.

------------

**Resuming TARDIS Simulations from HDF**

**Difficulty:** Hard

**Project Length:** Long

**Astronomy Knowledge Needed:** None

**Mentors:** Marc, Andrew

**Programming Skills Required** Python, Github

**GSoC Application Tag:** hdf

**Description:** Currently, TARDIS simulations run quickly and thus pausing and resuming a simulation is not necessary.
However, future additions to the code may increase runtimes substantially, so we would like to implement a way to save
and restart a TARDIS run arbitrarily. TARDIS produces HDF files of simulation results, so a similar method to save the
in-progress simulation would be appropriate. Pickling is not reliable for our custom classes. When pausing and writing
to file occurs should be determined by the end user at runtime.


**Your first objective if you choose to accept the mission:** Save an HDF file of the simulation and load it back to
plot results from the HDF file.


------------

**Monte Carlo 2D Packet Visualization**

**Difficulty:** Moderate

**Project Length:** Long

**Astronomy Knowledge Needed:** None

**Mentors:** Jaladh, Jack

**Programming Skills Required** Python, Github

**GSoC Application Tag:** mc_viz

**Description:**  TARDIS uses a monte carlo method to propagate photon packets through a model of an exploded star.  As
these virtual packets move through the ejecta model they interact with the gas through absorption, emission, and
scattering.  TARDIS currently has packet tracking capabilities to log the trajectories of packets during the
simulation, but this information is only stored in an ASCII datafile.  This project will build a visualization tool so
that scientists can see exactly how packets move through their models.

**Your first objective if you choose to accept the mission:**  Run a TARDIS simulation with packet logging enabled with
only 1 packet.  Plot the trajectory of the packet through the ejecta by graphing mu vs r.

------------

**Restructure Model Readers**

**Difficulty:** Moderate

**Astronomy Knowledge Needed:** None

**Mentors:** Marc Williamson, Jack O'Brien

**Programming Skills Required** Python, Jupyter

**GSoC Application Tag:** restructure

**Description:** TARDIS reads in many different data formats to compose its models. Currently, these functions and
classes are scattered across different files, making it difficult to understand the program flow and add new format
readers. There is also duplication of functionality. We would like these functions to be aggregated and restructured
to allow for future expansion and current maintenance.

**Your first objective if you choose to accept the mission:** Produce a consistent naming scheme for the TARDIS model
readers and CSVY parsers (notice the inconsistency already!).

------------

**Carsus Atomic Data**

**Difficulty:** Hard

**Astronomy Knowledge Needed:** Atomic Physics

**Mentors:** Andreas Flörs, Christian Vogl, Ezequiel Passaro

**Programming Skills Required:** Python

**GSoC Application Tag:** Carsus

**Description:** In addition to the input parameters (brightness of the supernova, ejected mass of the different
chemical elements, etc.), TARDIS requires data for describing the structure of atoms from different elements (e.g. a
sodium atom is differently structured than an iron atom; see the figure for a quick overview for carbon).

.. image:: {filename}images/bohrmodel.png
  :width: 400
  :alt: Alternative text

This data is not measured by astronomers but is most often gathered in a lab by atomic physicists. As measurement
equipment gets more and more precise, so do the measured structures of different elements. Thus these values update
from time to time and are often available in simple ASCII files (http://kurucz.harvard.edu/atoms/1401/gf1401.gam).
While we have compiled a small atom data set from some specific sources for our initial work, we would like to get a
collection of parsers that can read the different ASCII formats of the group and put this information in a uniform
database.

For this project, you would help us make parsers for a variety of formats from a collection of atomic data sources
(see the TEP) and in the second part put this into a database. The assembled database will not only be very interesting
for us, but also for many other fields of astronomy that do rely on atomic data. A useful resource of understanding
atomic structure description can be found in
http://www.physics.byu.edu/faculty/bergeson/physics571/notes/L27spectnotation.pdf.

We created a package that compiles all of this information into a database named Carsus
(see http://carsus.readthedocs.io/en/latest/). For this year we aim to strengthen the link between Carsus and TARDIS
and also include more atomic data into Carsus.

**Your first objective if you choose to accept the mission:** download the atomic data from
http://kookaburra.phyast.pitt.edu/hillier/web/CMFGEN.htm and read in the tabulated data contained in si2_osc_kurucz.
