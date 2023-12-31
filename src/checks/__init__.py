# pylint: disable=missing-module-docstring
from src.checks.PBP101_range_len import RangeLenNotAllowed
from src.checks.PBP102_json_dot_loads import JsonLoadsNotAllowed
from src.checks.PBP103_open_no_with import OpenNoWithNotAllowed
from src.checks.PBP104_requests_json_dumps import RequestsJsonDumpsNotAllowed
from src.checks.PBP105_assigns_to_list import AssignToListNotAllowed
from src.checks.PBP106_camel_case_func import CamelCaseFuncNotAllowed
from src.checks.PBP107_default_mutable_args import DefaultMutableArgsNotAllowed
from src.checks.PBP108_compares_types import CompareTypesNotAllowed
from src.checks.PBP109_compares_to_true import ComparedToTrueNotAllowed
from src.checks.PBP110_inherits_from_object import InheritsFromObjectNotAllowed
from src.checks.PBP111_not_using_ternary import NotUsingTernaryNotAllowed
from src.checks.PBP112_using_filter import UsingFilterOrMapNotAllowed
from src.checks.PBP113_shadow_builtins import ShadowBuiltinsNotAllowed
from src.checks.PBP114_no_pointless_ternary import NoPointlessTernaryNotAllowed
from src.checks.PBP115_better_any_and_all import AnyOrAllWithCompNotAllowed
from src.checks.PBP116_non_pascal_case_class import NonPascalCaseClassNotAllowed
from src.checks.PBP117_use_list_comp import NonUsingListCompNotAllowed

all_checks = [
    RangeLenNotAllowed, JsonLoadsNotAllowed, OpenNoWithNotAllowed, RequestsJsonDumpsNotAllowed,
    AssignToListNotAllowed, CamelCaseFuncNotAllowed, DefaultMutableArgsNotAllowed, CompareTypesNotAllowed,
    ComparedToTrueNotAllowed, InheritsFromObjectNotAllowed, NotUsingTernaryNotAllowed, UsingFilterOrMapNotAllowed,
    ShadowBuiltinsNotAllowed, NoPointlessTernaryNotAllowed, AnyOrAllWithCompNotAllowed, NonPascalCaseClassNotAllowed,
    NonUsingListCompNotAllowed,  # fmt: skip
]
