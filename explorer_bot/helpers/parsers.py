from argsparser import ArgsParser, ArgValsEnum
#players
playersParser = ArgsParser().addOption("ally", "a", ArgValsEnum.ONE)
#player
playerParser = ArgsParser().addOption("name", "n", ArgValsEnum.ONE)