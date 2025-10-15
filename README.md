# STOUT: SMILES to IUPAC name translator

Small molecules are represented by a variety of machine-readable strings (SMILES, InChi, SMARTS, among others). On the contrary, IUPAC (International Union of Pure and Applied Chemistry) names are devised for human readers. The authors trained a language translator model treating the SMILES and IUPAC as two different languages. 81 million SMILES were downloaded from PubChem and converted to SELFIES for model training. The corresponding IUPAC names for the 81 million SMILES were obtained with ChemAxon molconvert software.

This model was incorporated on 2023-01-05.Last packaged on 2025-10-15.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4se9`
- **Slug:** `smiles2iupac`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Chemical notation`, `Chemical language model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** IUPAC name of a specific SMILES

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| iupac_name | string | high | IUPAC name of the molecule |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4se9](https://hub.docker.com/r/ersiliaos/eos4se9)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4se9.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4se9.zip)

### Resource Consumption
- **Model Size (Mb):** `128`
- **Environment Size (Mb):** `2004`
- **Image Size (Mb):** `2344.41`

**Computational Performance (seconds):**
- 10 inputs: `51.46`
- 100 inputs: `-1`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/Kohulan/Smiles-TO-iUpac-Translator](https://github.com/Kohulan/Smiles-TO-iUpac-Translator)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00512-4](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00512-4)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [carcablop](https://github.com/carcablop)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4se9
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4se9
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
