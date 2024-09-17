from __init__ import close_connection, get_connection


class Band:
    def __init__(self, band_id):
        self.band_id = band_id
        self.conn = get_connection()

    def concerts(self):
        query = """
        SELECT * 
        FROM concerts 
        WHERE band_id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.band_id,))
            return cur.fetchall()

    def venues(self):
        query = """
        SELECT DISTINCT venues.* 
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.band_id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.band_id,))
            return cur.fetchall()

    def play_in_venue(self, venue_title, date):
        query = """
        INSERT INTO concerts (band_id, venue_id, date) 
        SELECT %s, venues.id, %s 
        FROM venues 
        WHERE venues.title = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.band_id, date, venue_title))
            self.conn.commit()

    def all_introductions(self):
        query = """
        SELECT venues.city, bands.name, bands.hometown 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.band_id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.band_id,))
            introductions = cur.fetchall()
            return [
                f"Hello {city}!!!!! We are {name} and we're from {hometown}"
                for city, name, hometown in introductions
            ]

    @staticmethod
    def most_performances():
        conn = get_connection()
        query = """
        SELECT bands.*, COUNT(concerts.id) AS performance_count 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        GROUP BY bands.id 
        ORDER BY performance_count DESC 
        LIMIT 1;
        """
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchone()
        close_connection(conn)
        return result

    def __del__(self):
        close_connection(self.conn)
