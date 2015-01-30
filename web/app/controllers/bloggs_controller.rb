class BloggsController < ApplicationController
  def index
    @articles = Blogg.all
  end

  def show
    @article = Blogg.find(params[:id])
  end

  def new
    @article = Blogg.new
  end

  def edit
    @article = Blogg.find(params[:id])
  end

  def create
    @article = Blogg.new(article_params)

    if @article.save
      redirect_to @article
    else
      render :new
    end
  end

  def update
    @article = Blogg.find(params[:id])

    if @article.update(article_params)
      redirect_to @article
    else
      render :edit
    end
  end

  private
  def article_params
    params.require(:blogg).permit(:title, :text)
  end
end
