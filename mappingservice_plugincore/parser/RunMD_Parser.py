from abc import abstractmethod

from mappingservice_plugincore.model.RunMD import RunMD
from mappingservice_plugincore.parser.MetadataParser import MetadataParser


class RunMD_Parser(MetadataParser):

    @abstractmethod
    def parse_run(self, payload) -> RunMD:
        """
        derives setup md from metadata file
        :param self:
        :param payload:
        :return:
        """
        pass