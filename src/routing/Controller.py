from src.ranking.RankingService import createRanking


def showRankings(country: str) -> str:
    return createRanking(country)
