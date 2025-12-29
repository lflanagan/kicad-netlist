from .traceformer_action import TraceformerPluginAction

# Register immediately so KiCad shows the toolbar button on load.
TraceformerPluginAction().register()
