import torch
from read_xyz import read_xyz

if __name__ == "__main__":
    hart2kcal = 627.509
    model = torch.jit.load('DLFFG2.pt')
    print(f"Force model version: {model.version} Copyright 2024 Wavefunction, Inc.")
    mols = read_xyz('input.xyz')

    for mol in mols:
        print(f"Read {mol.label}")
        Z = torch.tensor(mol.species,dtype=torch.int64)
        R = torch.tensor(mol.coords,dtype=torch.float32).unsqueeze(0) # add batch dimension
        res = model(Z,R,{'use_fit':True}) # our model processes one unique molecule at a time
        energy = hart2kcal*res[0][0]
        forces = (hart2kcal*res[1]).tolist()
        print(f"Energy (kcal/mol): {energy:.3f}")
        print("Forces (kcal/mol)/A:",[f"{f:.3f}" for f in forces])
