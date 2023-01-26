from flask_app.config.mysqlconnection import connectToMySQL

class PlayerReviews:
    db = "persona"
    def __init__(self,data):
        self.id = data['id']
        self.review = data['review']
        self.rating = data['rating']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_id = data['author_id']
        self.game_id = data['game_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO player_reviews (review, rating, author_id, game_id) VALUES(%(review)s,%(rating)s,%(author_id)s,%(game_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM player_reviews;"
        results = connectToMySQL(cls.db).query_db(query)
        reviews = []
        for row in results:
            reviews.append( cls(row))
        return reviews
    
    @classmethod
    def get_by_gameid(cls, data):
        query = "SELECT * FROM player_reviews WHERE game_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        reviews = []
        if results == 0:
            return reviews
        for row in results:
            reviews.append( cls(row))
        return reviews

        
#@app.route('/edit/review/<int:review_id>', methods=['GET', 'POST'])
#def edit_review(review_id):
    #review = Review.query.get(review_id)
    #if request.method == 'GET':
        #return render_template('GameRating.html', review=review)
   # else:
       # review.review = request.form['review']
        #review.rating = request.form['rating']
       # db.session.commit()
        #return redirect(url_for('index'))

#@app.route('/delete/review/<int:review_id>', methods=['POST'])
#def delete_review(review_id):
   # review = Review.query.get(review_id)
   # db.session.delete(review)
    #db.session.commit()
   # return redirect(url_for('index'))
        
    # @classmethod
    # def get_all_with_games(cls):
    #     games = Game.get_all();
    #     for game in games:
    #         for field in game:
    #             print(field)
    
    #     return 0



#@app.route('/delete/<int:games_id>')
#def delete_sighting(games_id):
    #if 'user_id' not in session:
        #return redirect('/logout')
    #data = { 
        #"id": games_id,
        #"posted_by": session['user_id']
    #}
    #games = games.delete_comment(data)
   # return redirect('/dashboard')  

# [game1[review1, review2,.....], game2, game3, ...]