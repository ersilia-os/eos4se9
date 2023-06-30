# STOUT: SMILES to IUPAC name translator

Small molecules are represented by a variety of machine-readable strings (SMILES, InChi, SMARTS, among others). On the contrary, IUPAC (International Union of Pure and Applied Chemistry) names are devised for human readers. The authors trained a language translator model treating the SMILES and IUPAC as two different languages. 81 million SMILES were downloaded from PubChem and converted to SELFIES for model training. The corresponding IUPAC names for the 81 million SMILES were obtained with ChemAxon molconvert software.

## Identifiers

* EOS model ID: `eos4se9`
* Slug: `smiles2iupac`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Text`
* Output Type: `String`
* Output Shape: `Single`
* Interpretation: IUPAC name of a specific SMILES

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00512-4)
* [Source Code](https://github.com/Kohulan/Smiles-TO-iUpac-Translator)
* Ersilia contributor: [carcablop](https://github.com/carcablop)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4se9)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4se9.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4se9) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00512-4) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!