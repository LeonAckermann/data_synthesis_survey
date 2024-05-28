
from .kddCup1999Dataset import KddCup1999Dataset
from .abaloneDataset import AbaloneDataset
from .adultDataset import AdultDataset
from .bankDataset import BankDataset
from .creditcardDataset import CreditcardDataset
from .diabetesDataset import DiabetesDataset
from .forestDataset import ForestDataset
from .magicDataset import MagicDataset


dataset_list = {
    "kddCup1999": KddCup1999Dataset,
    "abalone": AbaloneDataset,
    "adult": AdultDataset,
    "bank": BankDataset,
    "creditcard": creditcardDataset,
    "diabetes": diabetesDataset,
    "forest": ForestDataset,
    "magic": MagicDataset
}
