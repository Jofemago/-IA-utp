from aima3.agents import *



Ambiente = TrivialVacuumEnvironment()
asp = ReflexVacuumAgent()

Ambiente.add_thing(asp)

asp.location = Ambiente.default_location(asp)


TraceAgent(asp)
Ambiente.run(5)

print ('el performance es: ',asp.performance)
