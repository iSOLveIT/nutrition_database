
.. _core-deposition-1-OnLine-OnMessage:

===============================
OnLine and OnMessage Deposition
===============================


-------------------
Deposition Workflow
-------------------

A :ref:`depositor <terms-Depositor>` |_| registers information via:

1. :ref:`OnLine <terms-OnLine>` |_| interface, or

2. :ref:`OnMessage <terms-OnMessage>` |_| interface.

:ref:`OnTop <terms-OnTop>` |_| parser interacts with :ref:`ontologies <terms-Ontology>` to properly classify :ref:`deposit <terms-Deposit>`.

:ref:`USDA select <terms-USDA-Select>` |_| and :ref:`USDA prime <terms-USDA-Prime>` |_| data are complemented with data generated by :ref:`USDA mathematics <terms-USDA-Mathematics>`.

Ontomatica :ref:`graphs <terms-Graph>` |_| (representing things or events, and causal relationships between them) are updated.

Data then is stored on :ref:`MySQL <terms-MySQL>` |_| and :ref:`REST <terms-REST>` servers.

.. figure:: /_static/core-deposition-1-OnLine-OnMessage-1-process_.png
   :align: center

-----------------------------------------
Harmonization of GS1, GTIN and Vocal Data
-----------------------------------------

Explanation; equivalence :class:`schema:sameAs`.

.. csv-table::
   :header: "GS1 GPC Classes and Bricks", "Vocal facet term and facet term code"
   :widths: 15, 20

   "**Brick attribute: Classification**", "**Product Type**"
   "--", "[A0361]"
   "*Family: Fruits; Vegetables; Nuts; Seeds*", "*Fruits; Vegetables; Nuts; Seeds*"
   "[50100000]", "[A0987]"
   "*Class: Fruit - Prepared; Processed*", "*Fruit - Prepared; Processed*"
   "[50102000]", "[A0988]"
   "*Brick: Fruit - Prepared; Processed (Perishable)*", "*Fruit - Prepared; Processed (Perishable)*"
   "[10000205]", "[A0990]"
   "~~~", "~~~"
   "**Brick attribute: Formation**", "**Physical State, Shape or Form**"
   "[20000352]", "[E0113]"
   "*Chopped*", "*Divided into pieces*"
   "[30000653]", "[E0100]"
   "*Halved*", "*Divided into halves*"
   "[30001224]", "[E0116]"
   "*Homogenized*", "*Homogenized*"
   "[30001266]", "[H0306]"
   "~~~", "~~~"
   "**Brick attribute: Organic claim**", "**Consumer Group, Dietary Use, Label Claim**"
   "[20000142]", "[P0023]"
   "--", "*Organic food claim or use*"
   "--", "[P0128]"
   "*No*", "--"
   "[30002960]", "--"
   "*Yes*", "--"
   "[30002654]", "--"
   "~~~", "~~~"
   "**Brick attribute: If pitted, stoned**", "**Part of Plant/Fruit**"
   "[20000109]", "[C0167]"
   "*No*", "*Fruit, peel undetermined, core, pit or seed present*"
   "[30002960]", "[C0163]"
   "*Yes*", "*Fruit, peel undetermined, core, pit or seed removed*"
   "[30002654]", "[C0213]"
   "~~~", "~~~"
   "**Brick attribute: Cooking process**", "**Preservation Method**"
   "[20000128]", "[J0107]"
   "*Cooked*", "*Sterilized by heat*"
   "[30002953]", "[J0123]"
   "*Dried*", "*Dehydrated or dried*"
   "[30002762]", "[J0116]"
   "*Sugared*", "*Preserved by adding sugar*"
   "[30002518]", "[J0146]"
   "~~~", "~~~"
   "**Brick attribute: Refrigeration claim**", "**Preservation Method**"
   "[20000153]", "[J0107]"
   "*Can be refrigerated*", "*Preserved by chilling*"
   "[30000517]", "[J0131]"
   "*Must be refrigerated*", "--"
   "[30000090]", "--"
   "~~~", "~~~"
   "**Brick attribute: Type of fruit**", "**Fruit Producing Plant**"
   "[20000076] 103 possible types of fruits", "[B1140]"
   "*Apples*", "*Apple*"
   "[30003020]", "[B1245]"

---------------------------------------
Integration of GS1, GTIN and Vocal Data
---------------------------------------

OnMessage enables construction of a comprehensive food record that includes bar code information (GTIN) together with GS1 data (Brick codes), Vocal terms and related data.

.. figure:: /_static/core-deposition-1-OnLine-OnMessage-2-GTIN-Vocal_.png
   :align: center



.. |_| unicode:: 0x80

