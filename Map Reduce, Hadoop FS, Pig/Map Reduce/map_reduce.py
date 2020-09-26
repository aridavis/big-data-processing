from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingMapReducer(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.rating_mapper, reducer=self.rating_reducer)
        ]

    def rating_mapper(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split('\t')
        if (int(rating) > 3):
            yield int(rating), 1

    def rating_reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    RatingMapReducer().run()
