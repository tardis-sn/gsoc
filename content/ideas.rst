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
help with. Some of these we have specially selected for GSoC 2019 and are listed with specific “warm-up” tasks below.
But feel free to propose your own TEP and make a PR on that.

If you use one of our TEPs, you can definitely add more detail to the implementation, but what we really want to see is
a detailed timeline with milestones that shows us that you have thought about how to implement the feature in three
months. For any questions about the projects, please ask on `Gitter <https://gitter.im/tardis-sn/gsoc>`_\.

Putting in a Pull Request with the First objective is essential for each proposal to allow to see how you work.

------------

**Jupyter Notebook Widget for TARDIS**

**Difficulty:** Hard

**Astronomy Knowledge Needed:** None

**Mentors:** Wolfgang Kerzendorf, Marc Williamson

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

**Your first objective if you choose to accept the mission:** Make a Jupyter notebook and embed it in the documentation
that showcases the current way of running TARDIS and plots a spectrum.

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

**Quantity-ify TARDIS:**

**Difficulty:** Easy/Moderate

**Astronomy Knowledge Needed:** None

**Mentors:** ???

**Programming Skills Required:** Python, Pandas

**GSoC Application Tag:** dfq

**Description:** TARDIS frequently uses the Pandas.DataFrame and Pandas.Series data structures. However, these data
structures are not immediately compatible with storing the physical units associated with the numbers stored in the
structures. TARDIS puts a strong emphasis on both code readability and testing, and keeping track of the physical units
during internal calculations is extremely important towards both of these points of emphasis. The goal of this project
is to extend the Pandas data structures by adding meta data that stores the physical units. In addition, tests need to
be written to ensure that the units during internal calculations are consistent.

**Your first objective if you choose to accept the mission:** ???

