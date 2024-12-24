class Consensus:
    
    @staticmethod
    def is_chiain_valid(chain):
        
        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i-1]
            
            if current_block.pre_hash != previous_block.hash:
                return False
            
        return True
    
    @staticmethod
    def resolve_conflicts(local_chain, network_chains):
        
        new_chain = local_chain
        for chain in network_chains:
            if len(chain) > len(new_chain) and Consensus.is_chiain_valid(chain):
                new_chain = chain
            
        if new_chain != local_chain:
            print("updated with the longest valid chain from the network")
            
        else:
            print("Local chain is already the longest valid chain")
        
        return new_chain    
    