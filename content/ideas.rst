2020 Ideas Page
###############


:date: 2020-01-29
:modified: 2010-10-04 18:40
:tags: tardis, gsoc, ideas
:category: ideas page
:slug: tardis-gsoc-ideas
:authors: TARDIS-SN
:summary: Ideas Page

***************************
TARDIS GSoC 2020 Ideas Page
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
List of GSoC 2020 Project Ideas
*******************************

In the TARDIS collaboration we first establish a detailed plan on implementing new features before starting the actual
work. This is an important step that ensures that the entire TARDIS collaboration is informed about the development
efforts and that the team members can help shape the ideas during the discussion phase. We call these documents TEP -
TARDIS Enhancement Proposals. We already have a great list of ideas at https://github.com/tardis-sn/tep that we need
help with. Some of these we have specially selected for GSoC 2020 and are listed with specific “warm-up” tasks below.
But feel free to propose your own TEP and make a PR on that.

If you use one of our TEPs, you can definitely add more detail to the implementation, but what we really want to see is
a detailed timeline with milestones that shows us that you have thought about how to implement the feature in three
months. For any questions about the projects, please ask on `Gitter <https://gitter.im/tardis-sn/gsoc>`_\.

Putting in a Pull Request with the First objective is essential for each proposal to allow to see how you work.

------------

**Visualizing TARDIS flow through a graph**

**Difficulty:** Easy

**Astronomy Knowledge Needed:** None

**Mentors:** Marc Williamson, Christian Vogl

**Programming Skills Required:** Python, plotting preferred

**GSoC Application Tag:** network-graph

**Description:** TARDIS calculates the state of the gas of the exploding star in the plasma calculation. When the gas
changes temperature, TARDIS can automatically calculate what properties of the gas change. It uses a network graph for
this. This also allows us to visualize how the properties of the gas are calculated. This project will make an
interactive visualization of this process using networkx and matplotlib.

**Your first objective if you choose to accept the mission:** There already some parts of the visualization components
written for this project. You can find this here:
https://tardis-sn.github.io/tardis/api/tardis.plasma.base.html#tardis.plasma.base.BasePlasma.write_to_dot - try to
write the graph to a dotfile and then visualize with graphviz.

------------

**Jupyter Notebook Widget for TARDIS**

**Difficulty:** Hard

**Astronomy Knowledge Needed:** None

**Mentors:** Wolfgang Kerzendorf, Yssa Camacho

**Programming Skills Required:** Python, Jupyter

**Related TEP:** `TEP012 <https://github.com/tardis-sn/tep/blob/master/TEP012_gui_overhaul.rst>`_

**GSoC Application Tag:** jupyter-widget

**Description:** Often we need more information about the model and the calculation than the mere spectrum. For
example, we frequently need to investigate in detail how a specific spectral line feature forms, which ions and which
specific line transitions contribute. For exactly this purpose a Qt-GUI was developed
(see `here <https://tardis-sn.github.io/tardis/running/gui.html>`_\). It allows the user to
easily analyse TARDIS runs and extract important physical information without knowing the exact inner data structure of
TARDIS.

QT for this type of application is no longer the ideal framework. Many applications now work with Jupyter notebook and
we want to have a functional GUI that acts as a Jupyter widget. Once this is implemented, we would like to have several
example notebooks that exist within the documentation so that it is easy for users to try it out themselves.

**Your first objective if you choose to accept the mission:** Make a new Jupyter notebook and embed it in the documentation
that makes a bokeh plot (i.e. zoomable) of the spectrum in quickstart guide. Be creative in your approach, try to make it more interactive or add some new functionality taking inspiration from the GUI guide in docs.

------------

**Profile TARDIS**

**Difficulty:** Easy/Moderate

**Astronomy Knowledge Needed:** None

**Mentors:** Wolfgang Kerzendorf, Christian Vogl

**Programming Skills Required:** Python, Cython

**GSoC Application Tag:** asv

**Description:** TARDIS is a code that prides itself on being relatively fast to compute a synthetic spectrum. We are
also continuously adding additional microphysics in the code which sometimes requires additional calculation. It is
important to understand how much this microphyiscs adds to the runtime of the code. For this we want to implement a
benchmark in asv (airspeed velocity) that can automatically generate a report for us.

**Your first objective if you choose to accept the mission:** implement a simple benchmark in asv.

------------

**Quantity-ify TARDIS**

**Difficulty:** Easy/Moderate

**Astronomy Knowledge Needed:** None

**Mentors:** Marc Williamson

**Programming Skills Required:** Python, Pandas

**GSoC Application Tag:** dfq

**Description:** TARDIS frequently uses the Pandas.DataFrame and Pandas.Series data structures. However, these data
structures are not immediately compatible with storing the physical units associated with the numbers stored in the
structures. TARDIS puts a strong emphasis on both code readability and testing, and keeping track of the physical units
during internal calculations is extremely important towards both of these points of emphasis. The goal of this project
is to extend the Pandas data structures by adding meta data that stores the physical units. In addition, tests need to
be written to ensure that the units during internal calculations are consistent.

**Your first objective if you choose to accept the mission:** Write a simple extension of the Pandas.DataFrame that
keeps track of units for the dataframe. Ensure that the units persist through copying operations. You can use the
TARDIS IsotopeAbundances class for inspiration.

------------

**Integration Tests**

**Difficulty:** Easy

**Astronomy Knowledge Needed:** None

**Mentors:** Vytautas, Andreas

**Programming Skills Required:** Python, Azure Pipelines

**GSoC Application Tag:** integration-testing

**Description:**  Testing a scientific code like TARDIS is very important. We need to ensure that the scientific
insights we gain using the code are not based on bugs. Open collaboration with GitHub is great, but the more people
work on the code the more opportunities there are to introduce bugs. Making sure that the code doesn't change or only
changes as we expect it, is thus an important part of TARDIS development.

We have two types of tests: unit tests that verify small portions of the code and full-scale integration tests. Both of
these test types are implemented with a framework. But the integration tests are difficult to use.

* currently we mainly run the integration tests on an external server. We want to integrate them into our general Azure Pipeline continuous integration routine. We'd also like to expand that and check also different properties of our model against reference data (e.g. electron densities, ionization fractions, dilution factors)

* hand in hand with expanding the verification process we will improve the reporting process which should contain detailed plots and comparison results. A framework exists but is currently not actively used.

**Your first objective if you choose to accept the mission:** Run the integration tests as described here:
https://tardis-sn.github.io/tardis/development/running_tests.html

------------

**Optimisation with Numba**

**Difficulty:** Moderate

**Astronomy Knowledge Needed:** None

**Mentors:** Alice Harpole, Wolfgang Kerzendorf

**Programming Skills Required:** Python

**GSoC Application Tag:** numba

**Description:** In order to optimize the execution of several computationally intensive parts of TARDIS, we currently
use Cython. This converts these parts of the code to C and compiles them ahead of time, significantly improving their
performance. However, while fast, Cython involves a lot of extra boilerplate code, making the code overall harder to
follow and more difficult to maintain. We would, therefore, like to convert this Cython code to Numba, a just-in-time
Python compiler that involves significantly less additional code to Cython but can achieve similar performance.

**Your first objective if you choose to accept the mission:** Modify the function intensity_black_body
(https://github.com/tardis-sn/tardis/blob/f4dc1f2e36cc0406c9b90f8255ec74083c6ffc51/tardis/util/base.py#L246-L270)
to be compiled with Numba.

------------

**Enable the Dask framework for parallel execution for TARDIS**

**Difficulty:** Hard

**Astronomy knowledge needed:** None

**Mentors:** Wolfgang Kerzendorf, Christian Vogl

**Programming skills:** Python, dask

**GSoC Application Tag:** dask

**Description:** Exploring different simulations of supernovae and comparing them with observations is one of the
important tasks of TARDIS. This means that TARDIS needs to be run many tens of thousand times with different inputs.
The Dask framework will allow TARDIS to be excecuted on multi-core systems and super-computers. This project aims to
combine TARDIS with dask to make it easy to run many iterations of TARDIS.

**Your first objective if you choose to accept the mission:** Use dask to run distributed TARDIS instances in parallel
on your system. Use http://distributed.dask.org/en/latest/client.html as a guide to make a simple example.

------------

**Carsus Atomic Data**

**Difficulty:** Hard

**Astronomy Knowledge Needed:** Atomic Physics

**Mentors:** Andreas Flörs, Christian Vogl

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
