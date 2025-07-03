def spawn_agent(self, parentInstance: AgentInstance, agent_type: AgentarAgent, fields=None):
    if self.terminated.is_set():
        return None
    
    agetn_instance = deepcopy(self.agents_decl.get(agent_type))

    
    declared_types = list(self.agents_decl[agent_type]._fields_type.values())
    # if len(declared_types) != len(fields): # Check if the number of fields matches the declared types
    #     raise ValueError(f"Agent '{agent_type}' expects {len(declared_types)} fields, got {len(fields)}")
    for i, field in enumerate(fields): # Check if each field matches the declared type
        if type(field) != declared_types[i]:
            raise ValueError(f"Field {i}: got {type(field).__name__}, expected {declared_types[i].__name__}")
        
    id = parentInstance._id.child(parentInstance._next_child)     # Create new AgentId for the child agent
    parentInstance._next_child += 1                              # Increment child index for next spawn
    parentInstance._children.append(id)                          # Add child id to parent's children list
    new_agent_inst = deepcopy(self.agents_decl[agent_type])               # Get the agent declaration from the system
    agent = AgentInstance(new_agent_inst, system=self, id=id, fields=fields)
    
    with self._lock:
        self.agents[id.path] = agent
        self.threads[id.path] = AgentRunner(agent, system=self, agent_id=id)
        self.threads[id.path].start()
    return id