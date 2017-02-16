Welcome to django-notify's documentation!
=========================================

django-notify is a Django plug-in for automatically publishing AMQP events when models are modified.

Adding a notification event is as simple as adding an ``@notify`` decorator to your model class. By default, the decorator will publish an event for any ``create``, ``read``, ``update`` and ``delete`` (CRUD) action on your model.

.. code-block:: python

    @notify
    class MyModel(models.Model):
        pass

This behaviour can be modified to selectively act upon any combination of CRUD events:

.. code-block:: python

    @notify(when='CD')
    class MyModel(models.Model):
        pass

To specify which fields should be included in the AMQP body; add it to fields:

.. code-block:: python

    @notify(when='CRUD', fields=('pk', 'name'))
    class MyModel(models.Model):
        name = models.CharField()

That's it! For further configuration options such as generating custom routing keys for your events, see the :doc: `concepts` page.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   content/ideas
   content/concepts



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
