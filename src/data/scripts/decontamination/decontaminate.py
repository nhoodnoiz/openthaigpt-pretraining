from openthaigpt_pretraining_data.decontamination.decontamintate import decontaminate
from openthaigpt_pretraining_data.decontamination.generate_minhash import (
    generate_minhash,
)

import hydra


@hydra.main(version_base=None, config_path="./config", config_name="decontamination")
def main(cfg):
    generate_minhash(cfg.datasets, cfg.train_dataset, cfg.minhash)
    decontaminate(cfg.datasets, cfg.train_dataset, cfg.decontaminate)


if __name__ == "__main__":
    main()  # type: ignore
